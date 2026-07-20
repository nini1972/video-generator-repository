"""
Per-scene speech synthesis using Gemini's native audio generation.

Uses the same GEMINI_API_KEY already configured — no new credentials needed.
Follows the same content-hash caching pattern as image generation to prevent
stale files across runs with different screenplays.
"""

import os
import hashlib
import base64
import wave
from concurrent.futures import ThreadPoolExecutor
from typing import Optional
from google import genai
from google.genai import types


class SpeechSynthesiser:
    """Generates per-scene narration audio using Gemini's native audio generation."""

    # Cinematic voice options — Gemini prebuilt voices
    # Aoede: warm, resonant female voice with dramatic range
    VOICE_NARRATOR = "Aoede"  # Gemini prebuilt voice for cinematic narration

    _AUDIO_MODELS = [
        "gemini-2.5-flash-preview-tts",   # confirmed working
        "gemini-3.1-flash-tts",            # future availability
    ]
    # Safety: truncate narration before TTS to prevent oversized audio files
    MAX_NARRATION_CHARS = 300
    MAX_SPEECH_DURATION_SECONDS = 90
    SCENE_VISUAL_TAIL_SECONDS = 0.75

    # Fallback emotional arc — used only when Director doesn't provide emotional_tone
    _EMOTIONAL_ARC_FALLBACK = {
        "first": "somber, reflective, and quietly mysterious. Speak with a sense of loss and longing, as if surveying ruins.",
        "middle_early": "curious and gently awed. Speak with growing wonder, as if witnessing something extraordinary taking shape.",
        "middle_late": "urgent and intense. Speak with controlled tension, conveying high stakes and rapid action without shouting.",
        "last": "warm, triumphant, and deeply moved. Speak with quiet awe and satisfaction, as if witnessing a miracle.",
    }

    def __init__(self, client: Optional[genai.Client] = None):
        self.client: Optional[genai.Client]
        api_key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
        self.client = client or (genai.Client(api_key=api_key) if api_key else None)

    def synthesise_scene(self, narration_text: str, scene_num: int,
                         output_dir: str, voice: Optional[str] = None,
                         total_scenes: int = 4,
                         narration_voice: Optional[str] = None,
                         emotional_tone: Optional[str] = None) -> str | None:
        """
        Generates a .wav file for a single scene's narration.
        Uses content-hash naming to enable caching without staleness.
        
        Args:
            narration_text: The narration text to speak
            scene_num: Scene number (1-indexed)
            output_dir: Directory to save the audio file
            voice: Override voice name (default: Aoede)
            total_scenes: Total number of scenes for arc position
            narration_voice: Optional voice direction from the creative brief
            emotional_tone: Director-generated emotional direction for this scene
        
        Returns the local file path, or None on failure.
        """
        if not self.client or not narration_text or not narration_text.strip():
            return None

        voice = voice or self.VOICE_NARRATOR

        # Truncate long narrations at sentence boundary to prevent TTS overload
        narration_trimmed = self._truncate_narration(narration_text)

        # Determine emotional direction: prefer Director's emotional_tone,
        # fall back to position-based interpolation
        if emotional_tone:
            emotion = emotional_tone
        else:
            emotion = self._get_fallback_emotion(scene_num, total_scenes)

        # Build voice direction: use creative brief's narration_voice if provided
        voice_direction = narration_voice or "a cinematic film narrator"
        os.makedirs(output_dir, exist_ok=True)

        # Content-hash filename — include all performance direction for cache invalidation
        text_hash = hashlib.sha256(
            f"{narration_trimmed}|{voice}|{voice_direction}|{emotion}".encode("utf-8")
        ).hexdigest()[:16]
        wav_path = os.path.join(output_dir, f"scene_{scene_num}_speech_{text_hash}.wav")

        if os.path.exists(wav_path):
            if self._is_usable_speech(wav_path, scene_num, remove_invalid=True):
                print(f"[TTS] Scene {scene_num}: using cached speech ({text_hash}).")
                return wav_path

        print(f"[TTS] Scene {scene_num}: generating narration ({len(narration_trimmed)} chars)...")

        prompt = (
            f"You are {voice_direction}. "
            f"You have a velvet, whispered, and deeply warm FEMALE voice with an ambient, poetic range. "
            f"Read the following text aloud AS IF narrating an abstract artistic piece about digital infrastructure. "
            f"Your emotional tone for this scene should be: {emotion} "
            f"IMPORTANT PERFORMANCE DIRECTION: "
            f"Speak exceptionally slowly. Treat lines of code and data repositories like constellations. "
            f"Vary your pacing — linger on technical terms as if they are ancient incantations. "
            f"Use dynamic volume — whisper softly for mystery and complexity. "
            f"Let emotion and atmosphere color every word — this is NOT a flat documentation or corporate video reading. "
            f"Pause deeply and dramatically between clauses. "
            f"Read every single word of the text exactly — do not omit punctuation cues.\n\n"
            f"{narration_trimmed}"
        )

        for model in self._AUDIO_MODELS:
            try:
                response = self.client.models.generate_content(
                    model=model,
                    contents=prompt,
                    config=types.GenerateContentConfig(
                        response_modalities=["AUDIO"],
                        speech_config=types.SpeechConfig(
                            voice_config=types.VoiceConfig(
                                prebuilt_voice_config=types.PrebuiltVoiceConfig(
                                    voice_name=voice
                                )
                            )
                        ),
                    ),
                )

                # Guard against empty/filtered response
                if (not response.candidates
                        or not response.candidates[0].content
                        or not response.candidates[0].content.parts):
                    print(f"[TTS] Scene {scene_num}: {model} returned empty response (possibly filtered). Retrying...")
                    continue

                # Extract audio data from response
                for part in response.candidates[0].content.parts:
                    inline_data = part.inline_data
                    if inline_data is not None and inline_data.data is not None:
                        audio_data = inline_data.data
                        if isinstance(audio_data, str):
                            audio_bytes = base64.b64decode(audio_data)
                        else:
                            audio_bytes = bytes(audio_data)

                        mime_type = str(getattr(inline_data, 'mime_type', '') or '')

                        # Save audio — handle both WAV and raw PCM formats
                        if mime_type.startswith("audio/wav") or audio_bytes[:4] == b'RIFF':
                            with open(wav_path, "wb") as f:
                                f.write(audio_bytes)
                        else:
                            # Raw PCM (linear16, 24kHz, mono) — wrap in WAV container
                            self._write_pcm_as_wav(audio_bytes, wav_path)

                        if self._is_usable_speech(wav_path, scene_num, remove_invalid=True):
                            file_size_kb = len(audio_bytes) // 1024
                            print(f"[TTS] Scene {scene_num}: saved successfully ({file_size_kb}KB).")
                            return wav_path

                        print(f"[TTS] Scene {scene_num}: {model} produced implausibly long audio. Retrying...")
                        break

                print(f"[TTS] Scene {scene_num}: {model} returned no audio part.")

            except Exception as e:
                err_short = str(e)[:120]
                print(f"[TTS] Scene {scene_num}: {model} failed — {err_short}")
                continue

        print(f"[TTS] Scene {scene_num}: all models failed, skipping speech.")
        return None

    def synthesise_all_scenes(self, scenes: list, output_dir: str,
                              speech_mode: str = "full_narration",
                              voice: Optional[str] = None,
                              narration_voice: Optional[str] = None) -> list:
        """
        Generates speech for all scenes in parallel.
        Respects speech_mode: 'full_narration', 'prologue_epilogue_only', 'no_speech'.
        Adds 'local_speech_path' to each scene dict in-place.
        
        Args:
            narration_voice: Optional voice direction from the creative brief
                             (e.g., 'Documentary narrator — measured, poetic, awed')
        """
        os.makedirs(output_dir, exist_ok=True)

        if speech_mode == "no_speech":
            for scene in scenes:
                scene["local_speech_path"] = None
            return scenes

        if not scenes:
            return scenes

        total_scenes = len(scenes)

        def _process_scene(scene):
            scene_num = scene.get("scene_number", 0)
            narration = scene.get("narration_text", "")
            scene_emotion = scene.get("emotional_tone", None)

            # Prologue/epilogue mode: only narrate first and last scenes
            if speech_mode == "prologue_epilogue_only":
                if scene_num != 1 and scene_num != total_scenes:
                    scene["local_speech_path"] = None
                    return

            path = self.synthesise_scene(
                narration, scene_num, output_dir,
                voice=voice,
                total_scenes=total_scenes,
                narration_voice=narration_voice,
                emotional_tone=scene_emotion,
            )
            scene["local_speech_path"] = path

        with ThreadPoolExecutor(max_workers=min(len(scenes), 4)) as executor:
            futures = [executor.submit(_process_scene, s) for s in scenes]
            for f in futures:
                f.result()  # Wait for all to complete

        return scenes

    def align_scene_durations_to_speech(self, scenes: list) -> list:
        """Extends scene durations so generated narration is never truncated."""
        for scene in scenes:
            speech_path = scene.get("local_speech_path")
            if not speech_path or not os.path.exists(speech_path):
                continue

            scene_num = scene.get("scene_number", 0)
            speech_duration = self._get_speech_duration(speech_path, scene_num)
            if speech_duration is None:
                scene["local_speech_path"] = None
                continue

            if speech_duration > self.MAX_SPEECH_DURATION_SECONDS:
                print(
                    f"[TTS] Scene {scene_num}: ignoring {speech_duration:.2f}s narration; "
                    f"maximum is {self.MAX_SPEECH_DURATION_SECONDS}s."
                )
                scene["local_speech_path"] = None
                continue

            planned_duration = float(scene.get("duration_seconds", 8.0))
            aligned_duration = max(
                planned_duration,
                speech_duration + self.SCENE_VISUAL_TAIL_SECONDS,
            )
            scene["speech_duration_seconds"] = round(speech_duration, 2)
            if aligned_duration > planned_duration:
                scene["duration_seconds"] = round(aligned_duration, 2)
                print(
                    f"[TTS] Scene {scene.get('scene_number')}: extended visual "
                    f"from {planned_duration:.2f}s to {aligned_duration:.2f}s "
                    "to fit narration."
                )

        return scenes

    def _is_usable_speech(self, speech_path: str, scene_num: int,
                          remove_invalid: bool = False) -> bool:
        """Returns whether a WAV has a plausible narration duration."""
        duration = self._get_speech_duration(speech_path, scene_num)
        if duration is not None and duration <= self.MAX_SPEECH_DURATION_SECONDS:
            return True

        if remove_invalid and os.path.exists(speech_path):
            os.remove(speech_path)
        return False

    @staticmethod
    def _get_speech_duration(speech_path: str, scene_num: int) -> float | None:
        """Reads a WAV duration, returning None for corrupt or unreadable files."""
        try:
            with wave.open(speech_path, "rb") as audio_file:
                return audio_file.getnframes() / audio_file.getframerate()
        except (OSError, wave.Error, ZeroDivisionError) as error:
            print(f"[TTS] Scene {scene_num}: could not measure speech duration: {error}")
            return None

    def _get_fallback_emotion(self, scene_num: int, total_scenes: int) -> str:
        """
        Position-based emotional interpolation for when the Director
        doesn't provide an emotional_tone. Supports any scene count.
        """
        if total_scenes <= 1:
            return self._EMOTIONAL_ARC_FALLBACK["last"]
        if scene_num == 1:
            return self._EMOTIONAL_ARC_FALLBACK["first"]
        if scene_num == total_scenes:
            return self._EMOTIONAL_ARC_FALLBACK["last"]
        # Middle scenes: interpolate between curious and urgent
        progress = (scene_num - 1) / (total_scenes - 1)
        if progress < 0.5:
            return self._EMOTIONAL_ARC_FALLBACK["middle_early"]
        else:
            return self._EMOTIONAL_ARC_FALLBACK["middle_late"]

    @staticmethod
    def _write_pcm_as_wav(pcm_data: bytes, output_path: str,
                          sample_rate: int = 24000, channels: int = 1,
                          sample_width: int = 2):
        """Wraps raw linear16 PCM bytes in a standard WAV container."""
        with wave.open(output_path, 'wb') as wf:
            wf.setnchannels(channels)
            wf.setsampwidth(sample_width)
            wf.setframerate(sample_rate)
            wf.writeframes(pcm_data)

    def _truncate_narration(self, text: str) -> str:
        """
        Truncates narration to MAX_NARRATION_CHARS at the last sentence
        boundary (period, exclamation, or question mark) to prevent the
        TTS model from generating excessively long audio.
        """
        text = text.strip()
        if len(text) <= self.MAX_NARRATION_CHARS:
            return text

        # Find the last sentence-ending punctuation before the limit
        truncated = text[:self.MAX_NARRATION_CHARS]
        for marker in ['. ', '! ', '? ']:
            last_pos = truncated.rfind(marker)
            if last_pos > 0:
                return truncated[:last_pos + 1]

        # Fallback: check for sentence-end at the very end of the slice
        if truncated[-1] in '.!?':
            return truncated

        # Last resort: cut at last space to avoid mid-word break
        last_space = truncated.rfind(' ')
        if last_space > 0:
            return truncated[:last_space] + '.'

        return truncated + '.'
