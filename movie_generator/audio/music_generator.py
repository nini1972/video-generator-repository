"""
Soundtrack generation using Google's Lyria 3 music model via the Interactions API.

Lyria 3 is a dedicated high-fidelity music generation model available through
the Gemini API. It uses a different API surface (client.interactions.create)
than text/image generation (client.models.generate_content).

Uses the same GEMINI_API_KEY already configured — no new credentials needed.
Content-hash naming prevents stale cache across different creative directions.
"""

import os
import hashlib
import base64
from typing import Any, Optional, cast
from google import genai


class MusicGenerator:
    """Generates background soundtrack using Google's Lyria 3 music model."""

    # Lyria 3 models:
    # - lyria-3-clip-preview: always generates 30s clips (fast)
    # - lyria-3-pro-preview: full-length songs, variable duration
    _MUSIC_MODELS = [
        "lyria-3-clip-preview",
        "lyria-3-pro-preview",
    ]
    _AUDIO_EXTENSIONS = (".mp3", ".wav", ".ogg", ".flac", ".m4a")

    def __init__(self, client: Optional[genai.Client] = None):
        self.client: Optional[genai.Client]
        if client:
            self.client = client
        else:
            api_key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
            self.client = genai.Client(api_key=api_key) if api_key else None

    def generate_soundtrack(self, final_music_prompt: str, style_label: str, mode: str,
                            duration: float, output_dir: str) -> str | None:
        """
        Generates a background music track matching the creative direction.

        Args:
            final_music_prompt: Direct creative-brief instruction for the soundtrack
            style_label: Concise storyboard label for logging and cache identity
            mode:     "instrumental_only", "with_lyrics", or "no_music"
            duration: Target duration in seconds (derived from scene durations)
            output_dir: Directory to save the generated file

        Returns:
            Local file path to the generated audio file, or None on failure/skip.
        """
        if mode == "no_music" or not self.client:
            return None

        os.makedirs(output_dir, exist_ok=True)

        # Content-hash filename
        style_hash = hashlib.sha256(
            f"{final_music_prompt}|{style_label}|{mode}|{duration:.0f}".encode("utf-8")
        ).hexdigest()[:16]
        soundtrack_base_path = os.path.join(output_dir, f"soundtrack_{style_hash}")
        for cache_extension in self._AUDIO_EXTENSIONS:
            cached_path = f"{soundtrack_base_path}{cache_extension}"
            if os.path.exists(cached_path):
                print(f"[MusicGen] Using cached soundtrack ({style_hash}).")
                return cached_path

        print(f"[MusicGen] Generating {duration:.0f}s soundtrack: {style_label}...")

        # Build the music generation prompt
        vocal_instruction = (
            "purely instrumental, no vocals or singing"
            if mode == "instrumental_only"
            else "with subtle vocal harmonies or lyrics"
        )

        prompt = (
            f"Create a {duration:.0f}-second soundtrack for a short film. "
            f"Creative direction: {final_music_prompt}. "
            f"The track should be {vocal_instruction}. "
            "Honor the supplied creative direction for its genre, pacing, emotional shape, "
            "and level of musical development."
        )

        for model in self._MUSIC_MODELS:
            try:
                # Lyria uses the Interactions API, not generate_content
                interaction = cast(
                    Any,
                    self.client.interactions.create(
                        model=model,
                        input=prompt,
                    ),
                )

                # Extract audio from the interaction response
                generated_audio = interaction.output_audio
                if generated_audio and generated_audio.data:
                    audio_data = generated_audio.data
                    # output_audio.data is base64-encoded
                    if isinstance(audio_data, str):
                        audio_bytes = base64.b64decode(audio_data)
                    else:
                        audio_bytes = bytes(audio_data)

                    generated_extension = self._get_audio_extension(
                        str(getattr(generated_audio, "mime_type", "") or ""), audio_bytes
                    )
                    if not generated_extension:
                        print(f"[MusicGen] {model} returned an unsupported audio format.")
                        continue

                    soundtrack_path = f"{soundtrack_base_path}{generated_extension}"
                    with open(soundtrack_path, "wb") as f:
                        f.write(audio_bytes)

                    file_size_kb = len(audio_bytes) // 1024
                    print(f"[MusicGen] Soundtrack saved successfully ({file_size_kb}KB, model={model}).")
                    return soundtrack_path

                print(f"[MusicGen] {model} returned no audio data.")

            except Exception as e:
                err_short = str(e)[:150]
                print(f"[MusicGen] {model} failed — {err_short}")
                continue

        print("[MusicGen] All models failed, proceeding without generated music.")
        return None

    @staticmethod
    def _get_audio_extension(mime_type: str, audio_bytes: bytes) -> str | None:
        """Returns a filename extension that matches the generated audio container."""
        normalized_mime_type = str(mime_type).split(";", 1)[0].strip().lower()
        mime_extensions = {
            "audio/flac": ".flac",
            "audio/m4a": ".m4a",
            "audio/mp4": ".m4a",
            "audio/mpeg": ".mp3",
            "audio/mp3": ".mp3",
            "audio/ogg": ".ogg",
            "audio/wav": ".wav",
            "audio/x-wav": ".wav",
        }
        if normalized_mime_type in mime_extensions:
            return mime_extensions[normalized_mime_type]

        if audio_bytes.startswith(b"RIFF"):
            return ".wav"
        if audio_bytes.startswith(b"OggS"):
            return ".ogg"
        if audio_bytes.startswith(b"fLaC"):
            return ".flac"
        if audio_bytes.startswith(b"ID3") or audio_bytes[:2] in (b"\xff\xfb", b"\xff\xf3", b"\xff\xf2"):
            return ".mp3"

        return None
