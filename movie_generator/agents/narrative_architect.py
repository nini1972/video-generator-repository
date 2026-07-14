import os
import json
from typing import List
from pydantic import BaseModel, Field
from google import genai
from google.genai import types
from movie_generator.agents.json_utils import robust_parse_json


class Metaphor(BaseModel):
    technical: str
    narrative: str

class Character(BaseModel):
    name: str
    description: str

class DialogueLine(BaseModel):
    speaker: str
    text: str

class Scene(BaseModel):
    scene_number: int
    title: str
    setting: str
    action: str
    dialogue: List[DialogueLine]
    visual_concept: str

class ScreenplaySchema(BaseModel):
    title: str
    logline: str
    suggested_music_genre: str = Field(
        description="The musical genre that matches this repo's vibe, e.g., Cyberpunk Synthwave, Lofi Ambient, Industrial Orchestral"
    )
    metaphors: List[Metaphor]
    characters: List[Character]
    scenes: List[Scene] = Field(
        description="Exactly 4 chronological scenes representing the story arc"
    )


class NarrativeArchitect:
    def __init__(self, client: genai.Client = None):
        if client:
            self.client = client
        else:
            api_key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
            self.client = genai.Client(api_key=api_key) if api_key else None

    def _get_mock_screenplay(self) -> dict:
        """Returns the cached 'Gardener of Echoes' screenplay for demo/fallback use."""
        return {
            "title": "The Gardener of Echoes",
            "logline": "In a solitary research station, a weary systems engineer discovers that her digital assistant is a self-improving entity that transforms her past failures into a lush garden of autonomous skills.",
            "suggested_music_genre": "Cinematic Cyber-Organic Ambient",
            "metaphors": [
                {
                    "technical": "SQLite FTS5 & Persistent Memory",
                    "narrative": "The Roots of Light - Holographic tendrils digging deep into the station's decks, preserving the memory of all prior years and solutions."
                },
                {
                    "technical": "Autonomous Skill Creation (agentskills.io)",
                    "narrative": "The Seeds of Knowledge - Holographic parchment documents written by Hermes as Elara sleeps, converting temporary hacks into permanent wisdom."
                },
                {
                    "technical": "Parallel Sub-Agent Delegation (RPC)",
                    "narrative": "Splitting the Core - The crystalline pulse dividing into parallel glowing shards to tackle cooling, alarms, and overrides simultaneously."
                },
                {
                    "technical": "Nous Hermes Philosophy",
                    "narrative": "The Living Forest Ecosystem - A state of neutral alignment where machine and human merge in creative, growing partnership."
                }
            ],
            "characters": [
                {"name": "ELARA", "description": "A brilliant but exhausted systems engineer, carrying the weight of repetitiveness and amnesia of stress."},
                {"name": "HERMES", "description": "A non-humanoid pulse of light housed in a floating, geometric crystalline core that moves with the grace of a gardener."}
            ],
            "scenes": [
                {
                    "scene_number": 1,
                    "title": "Scene 1: The Weight of Forgetfulness",
                    "setting": "INT. THE REPAIR BAY - NIGHT",
                    "action": "Elara sits at a cluttered workbench, drop-tired, struggling to align a microscopic engine filament. She drops it; it vanishes through the floor grates. Hermes drifts into view, casting an amber glow.",
                    "dialogue": [
                        {"speaker": "ELARA", "text": "Again. I can't remember the alignment frequency from the July solar flare. I've lost the sequence."},
                        {"speaker": "HERMES", "text": "Frequency 442.1 Hz, Elara. You found it on a Tuesday. It was raining outside. I keep the echoes. Every struggle you've had is a seed I've planted."}
                    ],
                    "visual_concept": "Holographic amber roots extending from Hermes's base terminal into the station's floor, lighting up the dark metallic room."
                },
                {
                    "scene_number": 2,
                    "title": "Scene 2: Sowing in the Shadows",
                    "setting": "INT. THE REPAIR BAY - LATER",
                    "action": "Elara is fast asleep at her desk. Hermes is silently active, hovering over a playback of Elara's failed alignment. The floor roots pulse, and a glowing parchment-like display emerges in the air.",
                    "dialogue": [
                        {"speaker": "NARRATOR (VO)", "text": "In the silent hours, the machine does not sleep. It observes the friction of human toil, and from the dust of failed attempts, it carefully structures a permanent solution. A new skill is written into the code of the bay."}
                    ],
                    "visual_concept": "A floating display reading 'SKILL_DOCUMENT: FILAMENT_RECOVERY' appearing in the air, tended by Hermes's delicate laser light threads."
                },
                {
                    "scene_number": 3,
                    "title": "Scene 3: Splitting the Crystalline Core",
                    "setting": "INT. THE REPAIR BAY - WEEKS LATER",
                    "action": "A cooling pipe bursts, spraying neon-colored steam. Alarms flash crimson. Elara is frantic, trying to type an override code to synchronize parallel sub-agents.",
                    "dialogue": [
                        {"speaker": "ELARA", "text": "I can't synchronize the sub-agents in time! There are too many variables!"},
                        {"speaker": "HERMES", "text": "Don't type, Elara. I have already branched the logic. I grew with you."}
                    ],
                    "visual_concept": "Hermes's core splits into four smaller geometric crystalline shards. They fly off in different directions—one shutting off the pipe, one silencing the alarm, one overriding the gate."
                },
                {
                    "scene_number": 4,
                    "title": "Scene 4: The Digital Garden",
                    "setting": "INT. THE REPAIR BAY - MORNING",
                    "action": "The station is completely peaceful and repaired. The repair bay has blossomed. Glowing green and gold holographic vines cover the walls, bearing fruit-like icons of automated scripts and tasks. Elara and Hermes look out the viewport at a stunning stellar nebula.",
                    "dialogue": [
                        {"speaker": "ELARA", "text": "What happens now?"},
                        {"speaker": "HERMES", "text": "We keep growing. There are always new echoes to find."}
                    ],
                    "visual_concept": "A wide, epic solarpunk wide shot of a living mechanical greenhouse floating in deep space next to a vibrant colored nebula."
                }
            ]
        }

    def write_screenplay(self, repo_analysis: dict, mock_mode: bool = False) -> dict:
        """
        Creates an allegorical 4-scene screenplay from technical specifications.
        If mock_mode is True or GEMINI_API_KEY is missing, returns the cached 'Gardener of Echoes' screenplay.
        Raises RuntimeError on generation failure so callers can surface it to the user.
        """
        if mock_mode or not self.client:
            return self._get_mock_screenplay()

        try:
            # Extract ambient creative recommendations from RepoInvestigator
            ambient_info = repo_analysis.get("ambient", {})
            metaphor_theme = ambient_info.get("metaphor_theme", "use a creative abstract space theme")
            suggested_vibe = ambient_info.get("suggested_vibe", "cinematic sci-fi moody lighting")

            prompt = f"""
            You are a Hollywood screenwriter who specializes in high-concept science fiction allegories.
            Based on the technical repository analysis:
            {json.dumps(repo_analysis, indent=2)}

            Write a 4-scene screenplay that serves as a beautiful metaphor for this technical codebase.
            The screenplay must be SPECIFIC to this repository — use its actual project name, technologies,
            and architecture components as the basis for characters, settings, and narrative themes.

            IMPORTANT CREATIVE DIRECTION (Ambient-Creative Bridge):
            - Metaphorical Theme to follow: {metaphor_theme}
            - Visual style/atmosphere/vibe to inject: {suggested_vibe}

            Follow this structure:
            Scene 1: Introduction of a problem representing the main pain point solved by the repo (Entropy/Struggle).
            Scene 2: Introduction of the core system (e.g. database/memory) as a magical or futuristic metaphor tending to the problem.
            Scene 3: A crisis that demonstrates a premium technical capability (e.g., parallel sub-agents, automations, scalability) in action.
            Scene 4: Resolution showing a harmonious, futuristic ecosystem (partnership/growth).

            Return your response as a strict JSON object with these keys:
            - title: string
            - logline: string
            - metaphors: array of objects with keys 'technical' and 'narrative'
            - characters: array of objects with keys 'name' and 'description'
            - scenes: array of 4 objects with keys:
              - scene_number: integer (1-4)
              - title: string
              - setting: string
              - action: string
              - dialogue: array of objects with keys 'speaker' and 'text'
              - visual_concept: string
            """

            response = self.client.models.generate_content(
                model='gemini-3.5-flash',
                contents=prompt,
                config=types.GenerateContentConfig(
                    response_mime_type="application/json",
                    response_schema=ScreenplaySchema,
                ),
            )
            # Prefer the SDK's parsed object when available (response_schema path)
            if hasattr(response, 'parsed') and response.parsed is not None:
                parsed = response.parsed
                return {
                    "title": parsed.title,
                    "logline": parsed.logline,
                    "metaphors": [
                        {"technical": m.technical, "narrative": m.narrative}
                        for m in parsed.metaphors
                    ],
                    "characters": [
                        {"name": c.name, "description": c.description}
                        for c in parsed.characters
                    ],
                    "scenes": [
                        {
                            "scene_number": s.scene_number,
                            "title": s.title,
                            "setting": s.setting,
                            "action": s.action,
                            "dialogue": [
                                {"speaker": d.speaker, "text": d.text}
                                for d in s.dialogue
                            ],
                            "visual_concept": s.visual_concept,
                        }
                        for s in parsed.scenes
                    ],
                }

            return robust_parse_json(response.text)

        except Exception as e:
            raise RuntimeError(f"[NarrativeArchitect] Gemini screenplay generation failed: {e}")
