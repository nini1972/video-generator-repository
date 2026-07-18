"""
Audio mixing engine — pre-mixes per-scene speech and background music
into a single master audio track using pydub.

Separates the mixing concern from FFmpeg so the assembler only needs
to do a simple video+audio mux. Content-hash naming prevents overwriting.
"""

import os
import hashlib

try:
    from pydub import AudioSegment
    from pydub.silence import detect_nonsilent
    PYDUB_AVAILABLE = True
except ImportError:
    PYDUB_AVAILABLE = False


class AudioMixer:
    """Pre-mixes per-scene speech and background music into a single master audio track."""

    SPEECH_DUCK_DB = -12     # Reduce music volume by 12dB under speech
    MUSIC_SOLO_DB = -3       # Music at -3dB when playing alone (no speech)
    FADE_IN_MS = 2000        # 2 second fade-in
    FADE_OUT_MS = 3000       # 3 second fade-out

    def mix_master_audio(
        self,
        scene_speech_paths: list,
        scene_durations: list,
        soundtrack_path: str | None,
        speech_mode: str,
        soundtrack_mode: str,
        output_dir: str,
    ) -> str | None:
        """
        Creates a single master audio track by mixing per-scene speech with
        background music.

        Content-hash naming prevents overwriting between runs.
        Returns path to the mixed .wav file, or None if no audio to mix.
        """
        if not PYDUB_AVAILABLE:
            print("[AudioMixer] pydub not installed — skipping audio mixing.")
            print("[AudioMixer] Install with: pip install pydub")
            return None

        has_speech = (
            speech_mode != "no_speech"
            and any(p for p in scene_speech_paths if p)
        )
        has_music = (
            soundtrack_mode != "no_music"
            and soundtrack_path
            and os.path.exists(soundtrack_path)
        )

        if not has_speech and not has_music:
            print("[AudioMixer] No audio sources available — silent movie.")
            return None

        os.makedirs(output_dir, exist_ok=True)

        # Content-hash filename
        hash_inputs = "|".join([
            str(scene_speech_paths),
            str(scene_durations),
            str(soundtrack_path),
            speech_mode,
            soundtrack_mode,
        ])
        mix_hash = hashlib.sha256(hash_inputs.encode("utf-8")).hexdigest()[:16]
        output_path = os.path.join(output_dir, f"mixed_audio_{mix_hash}.wav")

        if os.path.exists(output_path):
            print(f"[AudioMixer] Using cached mix ({mix_hash}).")
            return output_path

        print("[AudioMixer] Mixing master audio track...")

        # Build the speech timeline (concatenate per-scene speech with silence padding)
        speech_track = None
        if has_speech:
            speech_track = self._build_speech_timeline(scene_speech_paths, scene_durations)

        # Load soundtrack
        music_track = None
        if has_music:
            try:
                music_track = AudioSegment.from_file(soundtrack_path)
            except Exception as e:
                print(f"[AudioMixer] Failed to load soundtrack: {e}")

        # Calculate total duration from scene timings
        total_duration_ms = int(sum(scene_durations) * 1000)

        # Mix based on what we have
        if speech_track and music_track:
            master = self._mix_speech_and_music(speech_track, music_track, total_duration_ms)
        elif speech_track:
            master = speech_track
            # Pad to total duration if speech is shorter
            if len(master) < total_duration_ms:
                master = master + AudioSegment.silent(duration=total_duration_ms - len(master))
        elif music_track:
            # Music only — trim/loop to match video duration
            master = self._fit_to_duration(music_track, total_duration_ms)
            master = master + self.MUSIC_SOLO_DB
        else:
            return None

        # Apply fade-in and fade-out
        master = master.fade_in(min(self.FADE_IN_MS, len(master) // 2))
        master = master.fade_out(min(self.FADE_OUT_MS, len(master) // 2))

        # Export
        master.export(output_path, format="wav")
        file_size_kb = os.path.getsize(output_path) // 1024
        print(f"[AudioMixer] Master audio saved ({file_size_kb}KB, {len(master) / 1000:.1f}s).")
        return output_path

    def _build_speech_timeline(self, speech_paths: list, scene_durations: list) -> AudioSegment:
        """
        Concatenates per-scene speech segments, padding with silence to match
        scene durations. This ensures each scene's narration starts at the correct
        timestamp relative to the video.
        """
        timeline = AudioSegment.empty()

        for i, (path, duration) in enumerate(zip(speech_paths, scene_durations)):
            scene_duration_ms = int(duration * 1000)

            if path and os.path.exists(path):
                try:
                    speech = AudioSegment.from_file(path)
                    # If speech is shorter than scene, pad with silence
                    if len(speech) < scene_duration_ms:
                        padding = AudioSegment.silent(duration=scene_duration_ms - len(speech))
                        timeline += speech + padding
                    else:
                        # If speech is longer than scene, truncate
                        timeline += speech[:scene_duration_ms]
                except Exception as e:
                    print(f"[AudioMixer] Failed to load scene {i + 1} speech: {e}")
                    timeline += AudioSegment.silent(duration=scene_duration_ms)
            else:
                # No speech for this scene — fill with silence
                timeline += AudioSegment.silent(duration=scene_duration_ms)

        return timeline

    def _mix_speech_and_music(self, speech: AudioSegment, music: AudioSegment,
                              total_duration_ms: int) -> AudioSegment:
        """
        Overlays speech on music with automatic ducking.
        Music volume drops by SPEECH_DUCK_DB only during audible speech segments.
        """
        # Fit music to video duration
        music = self._fit_to_duration(music, total_duration_ms)

        # Pad speech to match music length if needed
        if len(speech) < len(music):
            speech = speech + AudioSegment.silent(duration=len(music) - len(speech))

        ducked_music = self._duck_music_for_speech(music, speech)

        # Overlay speech on ducked music
        return ducked_music.overlay(speech)

    def _duck_music_for_speech(self, music: AudioSegment, speech: AudioSegment) -> AudioSegment:
        """Reduces music only across non-silent narration intervals."""
        narration_ranges = detect_nonsilent(
            speech,
            min_silence_len=200,
            silence_thresh=-45,
        )
        if not narration_ranges:
            return music

        ducked_music = music
        for start_ms, end_ms in narration_ranges:
            start_ms = max(0, start_ms)
            end_ms = min(len(ducked_music), end_ms)
            if start_ms >= end_ms:
                continue
            ducked_segment = ducked_music[start_ms:end_ms] + self.SPEECH_DUCK_DB
            ducked_music = (
                ducked_music[:start_ms]
                + ducked_segment
                + ducked_music[end_ms:]
            )

        return ducked_music

    @staticmethod
    def _fit_to_duration(audio: AudioSegment, target_ms: int) -> AudioSegment:
        """Trims or loops audio to match the target duration."""
        if len(audio) >= target_ms:
            return audio[:target_ms]

        # Loop to fill duration
        result = audio
        while len(result) < target_ms:
            result += audio
        return result[:target_ms]
