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
from google import genai
from google.genai import types


class SpeechSynthesiser:
    """Generates per-scene narration audio using Gemini's native audio generation."""

    # Cinematic voice options — Gemini prebuilt voices
    # Charon: deep, authoritative — ideal for cinematic narration
    VOICE_NARRATOR = "Charon"

    _AUDIO_MODELS = [
        "gemini-2.5-flash-preview-tts",   # confirmed working
        "gemini-3.1-flash-tts",            # future availability
    ]
    # Safety: truncate narration before TTS to prevent oversized audio files
    MAX_NARRATION_CHARS = 300

    def __init__(self, client: genai.Client = None):
        if client:
            self.client = client
        else:
            api_key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
            self.client = genai.Client(api_key=api_key) if api_key else None

    def synthesise_scene(self, narration_text: str, scene_num: int,
                         output_dir: str, voice: str = None) -> str | None:
        """
        Generates a .wav file for a single scene's narration.
        Uses content-hash naming to enable caching without staleness.
        Returns the local file path, or None on failure.
        """
        if not self.client or not narration_text or not narration_text.strip():
            return None

        voice = voice or self.VOICE_NARRATOR

        # Truncate long narrations at sentence boundary to prevent TTS overload
        narration_trimmed = self._truncate_narration(narration_text)

        # Content-hash filename for cache dedup (hash the trimmed text)
        text_hash = hashlib.sha256(
            f"{narration_trimmed}|{voice}".encode("utf-8")
        ).hexdigest()[:16]
        wav_path = os.path.join(output_dir, f"scene_{scene_num}_speech_{text_hash}.wav")

        if os.path.exists(wav_path):
            print(f"[TTS] Scene {scene_num}: using cached speech ({text_hash}).")
            return wav_path

        print(f"[TTS] Scene {scene_num}: generating narration ({len(narration_trimmed)} chars)...")

        prompt = (
            f"Read the following text aloud as a cinematic movie narrator. "
            f"Use a measured, dramatic pace with appropriate pauses:\n\n"
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

                # Extract audio data from response
                for part in response.candidates[0].content.parts:
                    if part.inline_data is not None:
                        audio_data = part.inline_data.data
                        if isinstance(audio_data, str):
                            audio_bytes = base64.b64decode(audio_data)
                        else:
                            audio_bytes = audio_data

                        mime_type = getattr(part.inline_data, 'mime_type', '') or ''

                        # Save audio — handle both WAV and raw PCM formats
                        if mime_type.startswith("audio/wav") or audio_bytes[:4] == b'RIFF':
                            with open(wav_path, "wb") as f:
                                f.write(audio_bytes)
                        else:
                            # Raw PCM (linear16, 24kHz, mono) — wrap in WAV container
                            self._write_pcm_as_wav(audio_bytes, wav_path)

                        file_size_kb = len(audio_bytes) // 1024
                        print(f"[TTS] Scene {scene_num}: saved successfully ({file_size_kb}KB).")
                        return wav_path

                print(f"[TTS] Scene {scene_num}: {model} returned no audio part.")

            except Exception as e:
                err_short = str(e)[:120]
                print(f"[TTS] Scene {scene_num}: {model} failed — {err_short}")
                continue

        print(f"[TTS] Scene {scene_num}: all models failed, skipping speech.")
        return None

    def synthesise_all_scenes(self, scenes: list, output_dir: str,
                              speech_mode: str = "full_narration",
                              voice: str = None) -> list:
        """
        Generates speech for all scenes in parallel.
        Respects speech_mode: 'full_narration', 'prologue_epilogue_only', 'no_speech'.
        Adds 'local_speech_path' to each scene dict in-place.
        """
        os.makedirs(output_dir, exist_ok=True)

        if speech_mode == "no_speech":
            for scene in scenes:
                scene["local_speech_path"] = None
            return scenes

        total_scenes = len(scenes)

        def _process_scene(scene):
            scene_num = scene.get("scene_number", 0)
            narration = scene.get("narration_text", "")

            # Prologue/epilogue mode: only narrate first and last scenes
            if speech_mode == "prologue_epilogue_only":
                if scene_num != 1 and scene_num != total_scenes:
                    scene["local_speech_path"] = None
                    return

            path = self.synthesise_scene(narration, scene_num, output_dir, voice=voice)
            scene["local_speech_path"] = path

        with ThreadPoolExecutor(max_workers=min(len(scenes), 4)) as executor:
            futures = [executor.submit(_process_scene, s) for s in scenes]
            for f in futures:
                f.result()  # Wait for all to complete

        return scenes

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
