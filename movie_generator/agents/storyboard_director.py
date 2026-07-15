import os
import json
import base64
import hashlib
from typing import List
from concurrent.futures import ThreadPoolExecutor, as_completed
from pydantic import BaseModel
from google import genai
from google.genai import types
from movie_generator.agents.json_utils import robust_parse_json
from movie_generator.audio.speech_synthesiser import SpeechSynthesiser
from movie_generator.audio.music_generator import MusicGenerator


class _StoryboardScene(BaseModel):
    scene_number: int
    title: str
    duration_seconds: float
    visual_prompt: str
    narration_text: str
    creative_rationale: str  # Director's self-reflection: why these symbols were chosen


class _AudioDirection(BaseModel):
    soundtrack_mode: str  # Options: "instrumental_only", "with_lyrics", "no_music"
    speech_mode: str      # Options: "full_narration", "prologue_epilogue_only", "no_speech"
    soundtrack_style: str  # Description of desired artistic style, e.g. "somber synth with human operatic lyrics"


class _StoryboardSchema(BaseModel):
    aesthetic_style: str
    audio_direction: _AudioDirection
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

        # Audio generation agents — share the same client/API key
        self.speech_synth = SpeechSynthesiser(client=self.client)
        self.music_gen = MusicGenerator(client=self.client)

    def _get_mock_storyboard(self, soundtrack_pref: str = "auto", speech_pref: str = "auto") -> dict:
        """Returns the cached Flowith storyboard with exact asset URLs for demo/fallback use."""
        return {
            "aesthetic_style": "Cyber-Organic, Solarpunk-meets-Cyberpunk, moody bioluminescent lighting, gold and amber highlights, cinematic widescreen 16:9, hyper-realistic details",
            "audio_direction": {
                "soundtrack_mode": "instrumental_only" if soundtrack_pref == "auto" else soundtrack_pref,
                "speech_mode": "full_narration" if speech_pref == "auto" else speech_pref,
                "soundtrack_style": "Contemplative ambient electronic soundtrack, transitioning into a crescendo"
            },
            "storyboards": [
                {
                    "scene_number": 1,
                    "title": "Scene 1: The Silent Archive",
                    "duration_seconds": 8.0,
                    "visual_prompt": "Wide establishing shot of a weary engineer in a dark repair bay filled with silent Echo-Engines, a crystalline floating core casts amber glow. Dramatic rim lighting, volumetric fog, bioluminescent accents. Cinematic 16:9, photorealistic, solarpunk-meets-cyberpunk. No text or UI.",
                    "image_url": "https://r2-bucket.flowith.net/f/81d85c63c5c115db/silent_archive_digital_library_index_0.jpeg",
                    "video_url": "https://vg.flowith.net/tencent/1412218316-AigcVideoTask-1ce1c70bd45a69f4b4fce9bcd7be60a6t.mp4",
                    "narration_text": "In the cold corners of the repair bay, memory fades like steam. She is not alone.",
                    "creative_rationale": "The dark, cluttered repair bay represents a codebase without persistent memory — past solutions lost. The crystalline core (Hermes) is the SQLite FTS5 system, glowing amber like stored knowledge waiting to be recalled."
                },
                {
                    "scene_number": 2,
                    "title": "Scene 2: Tending the Seeds",
                    "duration_seconds": 10.0,
                    "visual_prompt": "Close-up of holographic root tendrils growing from a floor terminal, forming a glowing parchment document in mid-air. Golden hour backlight through station windows. Bioluminescent organic textures, particle effects. Cinematic 16:9, photorealistic. No text or UI.",
                    "image_url": "https://r2-bucket.flowith.net/f/34f6e6adeb92c89c/gardener_synthesis_neon_seed_index_1.jpeg",
                    "video_url": "https://vg.flowith.net/tencent/1412218316-AigcVideoTask-30a5dae27c3c3bfa04458479f2cb7d03t.mp4",
                    "narration_text": "While she rests, luminous roots of memory extend into the bay. Yesterday's failures become tomorrow's autonomous skills.",
                    "creative_rationale": "The root tendrils represent FTS5 search indexes spreading through data. The self-writing parchment is agentskills.io autonomously generating skill documents from observed patterns — knowledge growing organically without human intervention."
                },
                {
                    "scene_number": 3,
                    "title": "Scene 3: Splitting the Core",
                    "duration_seconds": 9.0,
                    "visual_prompt": "Dynamic wide shot of a crystalline core splitting into four geometric shards flying to different stations. Red emergency lighting, coolant spray, lens flare. High energy, motion blur. Cinematic 16:9, photorealistic, solarpunk-meets-cyberpunk. No text or UI.",
                    "image_url": "https://r2-bucket.flowith.net/f/bb6c653e88a926d4/hermes_agent_holographic_interface_index_1.jpeg",
                    "video_url": "https://vg.flowith.net/tencent/1412218316-AigcVideoTask-d6865d18738546a6d8645a9befe49982t.mp4",
                    "narration_text": "When crisis strikes, there is no panic. The core divides — handling alarms, coolants, and code in perfect synchronicity.",
                    "creative_rationale": "The shard-splitting visualises RPC parallel sub-agent delegation — one coordinator spawning independent workers. Four shards for four simultaneous tasks mirrors the ThreadPoolExecutor pattern in the actual code."
                },
                {
                    "scene_number": 4,
                    "title": "Scene 4: The Digital Garden",
                    "duration_seconds": 12.0,
                    "visual_prompt": "Epic wide pull-back shot of a living mechanical greenhouse with holographic vines bearing fruit-like skill icons. Two figures gaze at a stellar nebula through a viewport. Volumetric atmosphere, warm amber and green palette. Cinematic 16:9, photorealistic. No text or UI.",
                    "image_url": "https://r2-bucket.flowith.net/f/3f5c3e5396a695fe/digital_forest_bloom_scene_index_2.jpeg",
                    "video_url": "https://vg.flowith.net/tencent/1412218316-AigcVideoTask-e00438f240db580a5839a2df59cf2b1et.mp4",
                    "narration_text": "Morning brings a living sanctuary. The tool has become a partner — together, they grow.",
                    "creative_rationale": "The greenhouse ecosystem represents Hermes's multi-model, vendor-agnostic philosophy — diverse species (providers) thriving together. The fruit-icons are mature, reusable skills. Human and machine gazing outward symbolises neutral-alignment partnership."
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

    def direct(self, creative_brief: dict, mock_mode: bool = False, repo_slug: str = None, soundtrack_pref: str = "auto", speech_pref: str = "auto") -> dict:
        """
        Creates a storyboard from a creative brief, with self-reflection.
        The Director must justify every visual choice via creative_rationale.
        If mock_mode is True or GEMINI_API_KEY is missing, returns the cached Flowith storyboard.
        Raises RuntimeError on generation failure so callers can surface it to the user.
        """
        if mock_mode or not self.client:
            return self._get_mock_storyboard(soundtrack_pref=soundtrack_pref, speech_pref=speech_pref)

        pref_instructions = []
        if soundtrack_pref != "auto":
            pref_instructions.append(f"- USER CONSTRAINT on soundtrack_mode: You MUST output '{soundtrack_pref}' as the soundtrack_mode in audio_direction.")
        if speech_pref != "auto":
            pref_instructions.append(f"- USER CONSTRAINT on speech_mode: You MUST output '{speech_pref}' as the speech_mode in audio_direction.")
        
        pref_prompt_str = "\n".join(pref_instructions) if pref_instructions else ""

        # Build the symbol map reference for the prompt
        symbol_map = creative_brief.get("symbol_map", [])
        symbol_ref = "\n".join([
            f"  - {s['technical']} → {s['symbol']} (because: {s['why']})"
            for s in symbol_map
        ])

        # Build the scene arc seeds
        scene_arc = creative_brief.get("scene_arc", {})
        arc_ref = "\n".join([
            f"  Scene {i}: {scene_arc.get(f'scene_{i}_seed', 'No seed provided')}"
            for i in range(1, 5)
        ])

        try:
            prompt = f"""
            You are the DIRECTOR — the final creative authority on this cinematic short film.
            You have received a creative brief from the PromptArchitect. Your job is to
            transform it into a production-ready storyboard with precise visual directives,
            timing, narration, and audio configuration.

            CREATIVE BRIEF:
            Title: {creative_brief.get('title', 'Untitled')}
            Logline: {creative_brief.get('logline', '')}
            Tone: {creative_brief.get('tone', '')}
            Visual Anchors: {creative_brief.get('visual_anchors', '')}
            Music Direction: {creative_brief.get('music_direction', '')}
            Narration Voice: {creative_brief.get('narration_voice', '')}

            SYMBOL MAP — You MUST use these visual symbols in your scenes:
{symbol_ref}

            SCENE ARC SEEDS — Develop each scene from these starting points:
{arc_ref}

            YOUR DIRECTIVES:

            1. VISUAL PROMPTS — For each scene, write an ultra-detailed prompt optimized
               for text-to-image diffusion models (Imagen 3). Follow this structure:
               - Start with shot type: "Wide establishing shot", "Close-up", "Macro detail"
               - Include lighting: "dramatic rim lighting", "golden hour backlight"
               - Include atmosphere: "volumetric fog", "particle effects", "lens flare"
               - End with style anchors: "cinematic, 16:9 aspect ratio, photorealistic"
               - MUST include the visual symbols from the symbol map above
               - Do NOT include text, UI, typography, or watermarks in the image

            2. NARRATION — Write a voiceover for each scene:
               - CRITICAL LENGTH RULE: 2-3 short sentences maximum (under 250 characters)
               - Must fit within the scene's duration_seconds at ~2.5 words/second
               - Write as a documentary narrator — poetic, measured, awed
               - Do NOT repeat the symbol map descriptions — describe what the VIEWER sees and feels

            3. CREATIVE RATIONALE — For each scene, explain WHY you chose these visuals.
               This is your self-reflection as Director. Connect each visual choice back to
               a specific technical component from the symbol map. This proves the video
               genuinely represents the underlying codebase.

            4. AUDIO DIRECTION:
               - soundtrack_mode: 'instrumental_only', 'with_lyrics', or 'no_music'
               - speech_mode: 'full_narration', 'prologue_epilogue_only', or 'no_speech'
               - soundtrack_style: refine the music direction from the brief: "{creative_brief.get('music_direction', '')}"

            {pref_prompt_str}

            Return a strict JSON object with keys:
            - aesthetic_style: string
            - audio_direction: object (soundtrack_mode, speech_mode, soundtrack_style)
            - storyboards: array of 4 objects (scene_number, title, duration_seconds,
              visual_prompt, narration_text, creative_rationale)
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
                    "audio_direction": {
                        "soundtrack_mode": parsed.audio_direction.soundtrack_mode,
                        "speech_mode": parsed.audio_direction.speech_mode,
                        "soundtrack_style": parsed.audio_direction.soundtrack_style,
                    },
                    "storyboards": [
                        {
                            "scene_number": s.scene_number,
                            "title": s.title,
                            "duration_seconds": s.duration_seconds,
                            "visual_prompt": s.visual_prompt,
                            "narration_text": s.narration_text,
                            "creative_rationale": s.creative_rationale,
                        }
                        for s in parsed.storyboards
                    ],
                }
            else:
                result = robust_parse_json(response.text)

            # ── Resolve assets directory ──────────────────────────────────────────
            base_assets_dir = os.path.abspath(
                os.path.join(os.path.dirname(__file__), "..", "assets")
            )
            if repo_slug:
                assets_dir = os.path.join(base_assets_dir, "target_repos", repo_slug)
            else:
                assets_dir = base_assets_dir
                
            os.makedirs(assets_dir, exist_ok=True)

            # ── Extract audio direction for generation ────────────────────────────
            audio_dir = result.get("audio_direction", {})
            active_speech_mode = audio_dir.get("speech_mode", "full_narration")
            active_soundtrack_mode = audio_dir.get("soundtrack_mode", "instrumental_only")
            active_soundtrack_style = audio_dir.get("soundtrack_style", "cinematic ambient")

            # Compute total duration for the music generator
            total_duration = sum(
                s.get("duration_seconds", 8.0) for s in result["storyboards"]
            )

            # Pull music direction from the creative brief
            suggested_genre = creative_brief.get("music_direction", "Cinematic Ambient")

            # ── Run image, speech, and music generation in parallel ───────────────
            print("[StoryboardDirector] Launching parallel asset generation (images + speech + music)...")

            with ThreadPoolExecutor(max_workers=3) as pool:
                future_images = pool.submit(
                    self._generate_scene_images,
                    result["storyboards"], result["aesthetic_style"], assets_dir
                )
                future_speech = pool.submit(
                    self.speech_synth.synthesise_all_scenes,
                    result["storyboards"], assets_dir,
                    speech_mode=active_speech_mode
                )
                future_music = pool.submit(
                    self.music_gen.generate_soundtrack,
                    active_soundtrack_style, suggested_genre,
                    active_soundtrack_mode, total_duration, assets_dir
                )

                # Collect results — images and speech modify scenes in-place
                result["storyboards"] = future_images.result()
                future_speech.result()  # scenes updated in-place with local_speech_path
                local_music_path = future_music.result()

            # Store the local music path for the pipeline's AudioMixer
            result["local_music_path"] = local_music_path

            # Inject remote video fallback for the web player (images are local)
            result.setdefault("master_concat_video_url", _FALLBACK_VIDEO_URL)

            return result

        except Exception as e:
            raise RuntimeError(f"[StoryboardDirector] Gemini storyboard generation failed: {e}")
