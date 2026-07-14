import os
import json
import base64
import hashlib
from typing import List
from concurrent.futures import ThreadPoolExecutor  # <-- Parallel speed boost!
from pydantic import BaseModel
from google import genai
from google.genai import types
from movie_generator.agents.json_utils import robust_parse_json


class _StoryboardScene(BaseModel):
    scene_number: int
    title: str
    duration_seconds: float
    visual_prompt: str
    narration_text: str


class _StoryboardSchema(BaseModel):
    aesthetic_style: str
    storyboards: List[_StoryboardScene]

# Fallback audio/video URLs from the Flowith demo run.
# Used when real TTS/music generation is not yet wired in.
_FALLBACK_MUSIC_URL = "https://v3b.fal.media/files/b/0a9a8cb8/K0cxAgb2F5nkl5PvR2r9C_output.mp3"
_FALLBACK_SPEECH_URL = "https://v3b.fal.media/files/b/0a9a8cbc/NjDP_0GI1rwgTAYGRNJWu_speech.mp3"
_FALLBACK_VIDEO_URL = "https://r2-bucket.flowith.net/concat_1779012993538996307.mp4"


class StoryboardDirector:
    def __init__(self, client: genai.Client = None):
        if client:
            self.client = client
        else:
            api_key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
            self.client = genai.Client(api_key=api_key) if api_key else None

    def _get_mock_storyboard(self) -> dict:
        """Returns the cached Flowith storyboard with exact asset URLs for demo/fallback use."""
        return {
            "aesthetic_style": "Cyber-Organic, Solarpunk-meets-Cyberpunk, moody bioluminescent lighting, gold and amber highlights, cinematic widescreen 16:9, hyper-realistic details",
            "storyboards": [
                {
                    "scene_number": 1,
                    "title": "Scene 1: The Silent Archive",
                    "duration_seconds": 8.0,
                    "visual_prompt": "Weary engineer Elara stands in a dark repair bay filled with shimmering Echo-Engines as a crystalline floating core named Hermes appears casting an amber glow, cinematic sci-fi moody lighting bioluminescent aesthetics high-tech organic textures solarpunk-meets-cyberpunk 16:9 aspect ratio, slow zoom on her exhausted face to the glowing core",
                    "image_url": "https://r2-bucket.flowith.net/f/81d85c63c5c115db/silent_archive_digital_library_index_0.jpeg",
                    "video_url": "https://vg.flowith.net/tencent/1412218316-AigcVideoTask-1ce1c70bd45a69f4b4fce9bcd7be60a6t.mp4",
                    "narration_text": "In the cold corners of the repair bay, memory fades like steam. Elara sits amid a graveyard of silent engines, struggling to remember the vital patterns she solved years before. But she is not alone."
                },
                {
                    "scene_number": 2,
                    "title": "Scene 2: Tending the Seeds",
                    "duration_seconds": 10.0,
                    "visual_prompt": "At night Elara sleeps peacefully while Hermes pulses with light and holographic roots grow from the floor terminal forming a glowing document called FILAMENT_RECOVERY in the air, time-lapse effect of the roots spreading, cinematic sci-fi moody lighting bioluminescent aesthetics high-tech organic textures solarpunk-meets-cyberpunk 16:9 aspect ratio",
                    "image_url": "https://r2-bucket.flowith.net/f/34f6e6adeb92c89c/gardener_synthesis_neon_seed_index_1.jpeg",
                    "video_url": "https://vg.flowith.net/tencent/1412218316-AigcVideoTask-30a5dae27c3c3bfa04458479f2cb7d03t.mp4",
                    "narration_text": "While she rests, Hermes begins its quiet work. Deep, luminous roots of persistent memory extend into the bay, turning the dry soil of yesterday's failures into fresh, autonomous skill documents."
                },
                {
                    "scene_number": 3,
                    "title": "Scene 3: Splitting the Core",
                    "duration_seconds": 9.0,
                    "visual_prompt": "Crisis unfolds with red lights flashing and coolant spraying as Hermes core splits into four smaller geometric shards that fly to different stations performing multiple tasks simultaneously, dynamic wide shot, cinematic sci-fi moody lighting bioluminescent aesthetics high-tech organic textures solarpunk-meets-cyberpunk 16:9 aspect ratio",
                    "image_url": "https://r2-bucket.flowith.net/f/bb6c653e88a926d4/hermes_agent_holographic_interface_index_1.jpeg",
                    "video_url": "https://vg.flowith.net/tencent/1412218316-AigcVideoTask-d6865d18738546a6d8645a9befe49982t.mp4",
                    "narration_text": "When crisis strikes and the bay fractures, there is no panic. With speed born of parallel execution, the core divides, handling alarms, coolants, and code in perfect synchronicity."
                },
                {
                    "scene_number": 4,
                    "title": "Scene 4: The Digital Garden",
                    "duration_seconds": 12.0,
                    "visual_prompt": "Peaceful resolution shows the bay transformed into a lush digital garden of glowing holographic vines and fruit where Elara and Hermes look out a viewport at a nebula, slow pull-back into wide cinematic shot of the station as part of a celestial landscape, cinematic sci-fi moody lighting bioluminescent aesthetics high-tech organic textures solarpunk-meets-cyberpunk 16:9 aspect ratio",
                    "image_url": "https://r2-bucket.flowith.net/f/3f5c3e5396a695fe/digital_forest_bloom_scene_index_2.jpeg",
                    "video_url": "https://vg.flowith.net/tencent/1412218316-AigcVideoTask-e00438f240db580a5839a2df59cf2b1et.mp4",
                    "narration_text": "Morning brings a living sanctuary. The mechanical graveyard has blossomed into a self-improving garden. The tool has become a partner, and together, they look toward a new horizon of endless growth."
                }
            ],
            "master_music_url": _FALLBACK_MUSIC_URL,
            "master_speech_url": _FALLBACK_SPEECH_URL,
            "master_concat_video_url": _FALLBACK_VIDEO_URL
        }

    def _generate_single_image(self, scene: dict, aesthetic_style: str, assets_dir: str) -> None:
        """Generates an image for a single scene using Gemini Image models."""
        scene_num = scene.get("scene_number", 0)
        
        # Inject overall aesthetic style into visual prompt for temporal consistency
        raw_prompt = scene.get("visual_prompt", "")
        compiled_prompt = f"{raw_prompt}, in the style of {aesthetic_style}, highly consistent"

        # Hash prompt to generate a unique cache filename
        prompt_hash = hashlib.sha256(compiled_prompt.encode("utf-8")).hexdigest()[:16]
        img_path = os.path.join(
            assets_dir, f"scene_{scene_num}_{prompt_hash}.png"
        )
        
        # Re-use cached image to avoid regenerating on server restart
        if os.path.exists(img_path):
            print(f"[ImageGen] Scene {scene_num}: using cached image ({prompt_hash}).")
            scene["local_image_path"] = img_path
            return

        print(f"[ImageGen] Scene {scene_num}: generating image...")
        
        _IMAGE_MODELS = [
            "gemini-2.5-flash-image",
            "gemini-3.1-flash-image",
            "gemini-3.1-flash-image-preview",
        ]

        for model in _IMAGE_MODELS:
            try:
                response = self.client.models.generate_content(
                    model=model,
                    contents=compiled_prompt,
                    config=types.GenerateContentConfig(
                        response_modalities=["IMAGE", "TEXT"],
                    ),
                )
                for part in response.candidates[0].content.parts:
                    if part.inline_data is not None:
                        img_data = part.inline_data.data
                        if isinstance(img_data, str):
                            img_bytes = base64.b64decode(img_data)
                        else:
                            img_bytes = img_data
                        with open(img_path, "wb") as fh:
                            fh.write(img_bytes)
                        scene["local_image_path"] = img_path
                        print(f"[ImageGen] Scene {scene_num}: saved successfully ({len(img_bytes)//1024}KB).")
                        break
                if "local_image_path" in scene:
                    break
                print(f"[ImageGen] Scene {scene_num}: {model} returned no image part.")
            except Exception as e:
                err_short = str(e)[:120]
                print(f"[ImageGen] Scene {scene_num}: {model} failed — {err_short}")
                continue

    def _generate_scene_images(self, scenes: list, aesthetic_style: str, assets_dir: str) -> list:
        """Runs image generations concurrently using a thread pool."""
        with ThreadPoolExecutor(max_workers=len(scenes)) as executor:
            futures = [
                executor.submit(self._generate_single_image, scene, aesthetic_style, assets_dir)
                for scene in scenes
            ]
            for future in futures:
                future.result()  # Wait for all images to complete
        return scenes

    def direct(self, screenplay: dict, mock_mode: bool = False, repo_slug: str = None) -> dict:
        """
        Creates a storyboard detailing scene visuals, precise timings, and narrations.
        If mock_mode is True or GEMINI_API_KEY is missing, returns the cached Flowith storyboard.
        Raises RuntimeError on generation failure so callers can surface it to the user.
        """
        if mock_mode or not self.client:
            return self._get_mock_storyboard()

        try:
            prompt = f"""
            You are a senior cinematic creative director.
            Based on the screenplay:
            {json.dumps(screenplay, indent=2)}

            Synthesize detailed visual directives and timing scripts for each of the 4 scenes.
            The visuals MUST be specific to the story in the screenplay provided — do not use generic imagery.
            Ensure the styling guidelines are rich and descriptive.
            Generate highly vivid prompts optimized for text-to-image and text-to-video diffusion models (e.g. Imagen 3).

            Return your response as a strict JSON object with these keys:
            - aesthetic_style: string (mood, color, lighting, framing, lens, atmosphere)
            - storyboards: array of 4 objects with keys:
              - scene_number: integer (1-4)
              - title: string
              - duration_seconds: float (recommend between 6.0 and 12.0 seconds)
              - visual_prompt: string (ultra-detailed keyframe generation prompt)
              - narration_text: string (narrator's voiceover for this specific scene)
            """

            response = self.client.models.generate_content(
                model='gemini-3.5-flash',
                contents=prompt,
                config=types.GenerateContentConfig(
                    response_mime_type="application/json",
                    response_schema=_StoryboardSchema,
                ),
            )
            # Prefer SDK-parsed object (response_schema path); fall back to text parser
            if hasattr(response, 'parsed') and response.parsed is not None:
                parsed = response.parsed
                result = {
                    "aesthetic_style": parsed.aesthetic_style,
                    "storyboards": [
                        {
                            "scene_number": s.scene_number,
                            "title": s.title,
                            "duration_seconds": s.duration_seconds,
                            "visual_prompt": s.visual_prompt,
                            "narration_text": s.narration_text,
                        }
                        for s in parsed.storyboards
                    ],
                }
            else:
                result = robust_parse_json(response.text)

            # Generate personalized scene images from each visual_prompt
            base_assets_dir = os.path.abspath(
                os.path.join(os.path.dirname(__file__), "..", "assets")
            )
            if repo_slug:
                assets_dir = os.path.join(base_assets_dir, "target_repos", repo_slug)
            else:
                assets_dir = base_assets_dir
                
            os.makedirs(assets_dir, exist_ok=True)
            result["storyboards"] = self._generate_scene_images(
                result["storyboards"], result["aesthetic_style"], assets_dir
            )

            # Inject audio/video fallbacks until real TTS and music generation is wired in.
            # These allow the video player to function even without an FFmpeg-assembled output.
            result.setdefault("master_music_url", _FALLBACK_MUSIC_URL)
            result.setdefault("master_speech_url", _FALLBACK_SPEECH_URL)
            result.setdefault("master_concat_video_url", _FALLBACK_VIDEO_URL)

            return result

        except Exception as e:
            raise RuntimeError(f"[StoryboardDirector] Gemini storyboard generation failed: {e}")
