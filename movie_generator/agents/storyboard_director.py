import os
import json
from google import genai
from google.genai import types

class StoryboardDirector:
    def __init__(self, client: genai.Client = None):
        self.client = client or (genai.Client() if os.environ.get("GEMINI_API_KEY") else None)

    def direct(self, screenplay: dict, mock_mode: bool = False) -> dict:
        """
        Creates a storyboard detailing scene visuals, precise timings, and narrations.
        If mock_mode is True or GEMINI_API_KEY is missing, returns the premium Flowith storyboard with exact asset URLs.
        """
        if mock_mode or not self.client:
            # We map actual high-quality JPEG and MP4 links from the Flowith run to ensure stunning visuals load immediately!
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
                "master_music_url": "https://v3b.fal.media/files/b/0a9a8cb8/K0cxAgb2F5nkl5PvR2r9C_output.mp3",
                "master_speech_url": "https://v3b.fal.media/files/b/0a9a8cbc/NjDP_0GI1rwgTAYGRNJWu_speech.mp3",
                "master_concat_video_url": "https://r2-bucket.flowith.net/concat_1779012993538996307.mp4"
            }

        # Real Storyboard Generation
        try:
            prompt = f"""
            You are a senior cinematic creative director.
            Based on the screenplay:
            {json.dumps(screenplay, indent=2)}
            
            Synthesize detailed visual directives and timing scripts for each of the 4 scenes.
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
                model='gemini-2.5-flash',
                contents=prompt,
                config=types.GenerateContentConfig(
                    response_mime_type="application/json",
                ),
            )
            return json.loads(response.text)

        except Exception as e:
            print(f"Error in StoryboardDirector: {e}. Falling back to mock storyboard.")
            return self.direct(screenplay, mock_mode=True)
