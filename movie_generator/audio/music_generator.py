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

    def __init__(self, client: genai.Client = None):
        if client:
            self.client = client
        else:
            api_key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
            self.client = genai.Client(api_key=api_key) if api_key else None

    def generate_soundtrack(self, style: str, genre: str, mode: str,
                            duration: float, output_dir: str) -> str | None:
        """
        Generates a background music track matching the creative direction.

        Args:
            style:    Descriptive style from audio_direction (e.g., "contemplative ambient electronic")
            genre:    Genre from screenplay (e.g., "Cinematic Cyber-Organic Ambient")
            mode:     "instrumental_only", "with_lyrics", or "no_music"
            duration: Target duration in seconds (derived from scene durations)
            output_dir: Directory to save the generated file

        Returns:
            Local file path to the generated .mp3, or None on failure/skip.
        """
        if mode == "no_music" or not self.client:
            return None

        os.makedirs(output_dir, exist_ok=True)

        # Content-hash filename
        style_hash = hashlib.sha256(
            f"{style}|{genre}|{mode}|{duration:.0f}".encode("utf-8")
        ).hexdigest()[:16]
        mp3_path = os.path.join(output_dir, f"soundtrack_{style_hash}.mp3")

        if os.path.exists(mp3_path):
            print(f"[MusicGen] Using cached soundtrack ({style_hash}).")
            return mp3_path

        print(f"[MusicGen] Generating {duration:.0f}s soundtrack: {style}...")

        # Build the music generation prompt
        vocal_instruction = (
            "purely instrumental, no vocals or singing"
            if mode == "instrumental_only"
            else "with subtle vocal harmonies or lyrics"
        )

        prompt = (
            f"A {duration:.0f}-second piece of {genre} music. "
            f"Style: {style}. "
            f"The track should be {vocal_instruction}. "
            f"This is the SCORE for a cinematic short film — "
            f"it MUST have dramatic emotional progression: "
            f"begin sparse and atmospheric, build tension in the middle, "
            f"swell to an emotional climax, then resolve warmly. "
            f"NOT static ambient — dynamic, with clear dramatic arc and evolving intensity."
        )

        for model in self._MUSIC_MODELS:
            try:
                # Lyria uses the Interactions API, not generate_content
                interaction = self.client.interactions.create(
                    model=model,
                    input=prompt,
                )

                # Extract audio from the interaction response
                generated_audio = interaction.output_audio
                if generated_audio and generated_audio.data:
                    audio_data = generated_audio.data
                    # output_audio.data is base64-encoded
                    if isinstance(audio_data, str):
                        audio_bytes = base64.b64decode(audio_data)
                    else:
                        audio_bytes = audio_data

                    with open(mp3_path, "wb") as f:
                        f.write(audio_bytes)

                    file_size_kb = len(audio_bytes) // 1024
                    print(f"[MusicGen] Soundtrack saved successfully ({file_size_kb}KB, model={model}).")
                    return mp3_path

                print(f"[MusicGen] {model} returned no audio data.")

            except Exception as e:
                err_short = str(e)[:150]
                print(f"[MusicGen] {model} failed — {err_short}")
                continue

        print("[MusicGen] All models failed, proceeding without generated music.")
        return None
