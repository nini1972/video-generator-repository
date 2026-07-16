"""
PromptArchitect — Creative Brief Generator & Symbol Grounding Agent.

Translates a RepoInvestigator's technical analysis into a creative brief
that grounds every visual symbol in an actual codebase component.

Replaces the NarrativeArchitect in the pipeline. Instead of writing a full
screenplay (with dialogue that was never used downstream), it produces a
tight creative brief: a symbol_map, scene visual seeds, tone, and a single
authoritative music direction.
"""

import os
import json
from typing import List, Optional
from pydantic import BaseModel, Field
from google import genai
from google.genai import types
from movie_generator.agents.json_utils import robust_parse_json


# ── Pydantic Output Schema ───────────────────────────────────────────────────

class SymbolMapping(BaseModel):
    technical: str = Field(description="The real technical component from the repo (e.g., 'WebSocket relay layer')")
    symbol: str = Field(description="The visual metaphor representing it (e.g., 'Luminous bridge filaments between star-nodes')")
    why: Optional[str] = Field(default=None, description="Optional explanation of the technical connection behind the visual metaphor")


class SceneSeed(BaseModel):
    scene_number: int = Field(default=1, description="Scene number (1-indexed)")
    dramatic_beat: Optional[str] = Field(default=None, description="The dramatic purpose of this scene (e.g., 'cold start', 'the spark', 'crisis', 'harmony')")
    visual_seed: str = Field(description="1-2 sentence visual concept for this scene")


class CreativeBriefSchema(BaseModel):
    title: str = Field(description="Cinematic title for the short film")
    logline: str = Field(description="One-sentence pitch (under 200 characters)")
    symbol_map: List[SymbolMapping] = Field(description="Technical component → visual symbol mappings with rationale")
    scene_arc: List[SceneSeed] = Field(min_length=2, max_length=8, description="Visual seeds for a renderable 2-8 scene arc")
    tone: str = Field(description="Emotional arc description (e.g., 'Contemplative wonder building to triumphant revelation')")
    visual_anchors: str = Field(description="Color palette and atmosphere keywords (e.g., 'Deep space indigo, bioluminescent cyan, warm amber')")
    music_direction: str = Field(description="Single authoritative music/soundtrack description for the entire film")
    narration_voice: str = Field(description="Voice direction for narration (e.g., 'Documentary narrator — measured, poetic, awed')")


class PromptArchitect:
    """
    Crafts a creative brief that maps a repository's architecture to
    visual symbols, ensuring every metaphor is grounded in real code.
    """

    def __init__(self, client: genai.Client = None, free_form: bool = False):
        if client:
            self.client = client
        else:
            api_key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
            self.client = genai.Client(api_key=api_key) if api_key else None
        self.free_form = free_form

    def _get_mock_brief(self) -> dict:
        """Returns a mock creative brief modelled on the Hermes Agent repo."""
        return {
            "title": "The Gardener of Echoes",
            "logline": "A weary engineer discovers her digital assistant has been quietly transforming her failures into a living garden of autonomous skills.",
            "symbol_map": [
                {
                    "technical": "SQLite FTS5 & Persistent Memory",
                    "symbol": "Holographic amber root tendrils extending through the station's floor, pulsing with stored light",
                    "why": "FTS5 indexes past conversations like roots absorbing nutrients — persistent, branching, and foundational to everything above."
                },
                {
                    "technical": "Autonomous Skill Creation (agentskills.io)",
                    "symbol": "Glowing parchment documents that self-write in mid-air, tended by delicate laser threads",
                    "why": "Skills are auto-generated documents born from observation of human struggle — the parchment metaphor captures their autonomous, knowledge-preserving nature."
                },
                {
                    "technical": "Parallel Sub-Agent Delegation (RPC)",
                    "symbol": "A crystalline core splitting into four geometric shards flying in different directions",
                    "why": "RPC sub-agents are independent parallel workers spawned from a single coordinator — shard-splitting captures the one-to-many delegation pattern."
                },
                {
                    "technical": "Nous Hermes Philosophy & Multi-Model Support",
                    "symbol": "A living mechanical greenhouse floating in deep space, blending organic and synthetic elements",
                    "why": "Hermes's neutral alignment and multi-vendor philosophy mirrors a greenhouse ecosystem — diverse, interconnected, vendor-agnostic growth."
                }
            ],
            "scene_arc": [
                {"scene_number": 1, "dramatic_beat": "cold start", "visual_seed": "A cluttered, dark repair bay — an exhausted engineer drops a critical component through the floor grates, unable to remember past solutions"},
                {"scene_number": 2, "dramatic_beat": "the spark", "visual_seed": "In the silent hours, the machine observes and writes — glowing parchment skill-documents emerge from the dust of failed attempts"},
                {"scene_number": 3, "dramatic_beat": "crisis", "visual_seed": "A cooling pipe bursts, alarms flash crimson — the crystalline core splits into parallel shards to handle multiple emergencies simultaneously"},
                {"scene_number": 4, "dramatic_beat": "harmony", "visual_seed": "Morning reveals a living greenhouse — holographic vines bearing fruit-like icons of automated scripts, engineer and machine gazing at a nebula"}
            ],
            "tone": "Melancholic wonder building through quiet determination to harmonious revelation",
            "visual_anchors": "Solarpunk-meets-cyberpunk, bioluminescent amber and green accents, moody dark metallic interiors opening to cosmic vistas",
            "music_direction": "Contemplative ambient electronic soundtrack with organic cello swells, transitioning from sparse minimalism to a warm crescendo",
            "narration_voice": "Cinematic film narrator — dramatic, with dynamic range. Intense whisper for mystery, powerful projection for triumph. NOT a flat documentary read."
        }

    def craft_brief(self, repo_analysis: dict, mock_mode: bool = False, free_form: Optional[bool] = None) -> dict:
        """
        Translates a RepoInvestigator's technical analysis into a creative brief.
        Every visual symbol is explicitly tied to a real repo component.

        Args:
            repo_analysis: Output from RepoInvestigator.analyze()
            mock_mode: If True, returns the cached Hermes Agent brief
            free_form: If True, relaxes structural constraints (defaults to self.free_form)

        Returns:
            Creative brief dict with symbol_map, scene_arc, tone, etc.

        Raises:
            RuntimeError on generation failure.
        """
        # Use instance-level free_form if not explicitly provided
        if free_form is None:
            free_form = self.free_form

        if mock_mode or not self.client:
            return self._get_mock_brief()

        try:
            # Extract ambient creative hints from Stage 1
            ambient_info = repo_analysis.get("ambient", {})
            metaphor_theme = ambient_info.get("metaphor_theme", "use a creative abstract metaphor")
            suggested_vibe = ambient_info.get("suggested_vibe", "cinematic sci-fi moody lighting")
            suggested_genre = ambient_info.get("suggested_music_genre", "cinematic ambient soundtrack")

            prompt = f"""
            You are a Creative Translator — a unique hybrid of a film production designer
            and a software architect. Your job is to translate a codebase's technical
            architecture into a visual language for a ~40-second cinematic short film.

            Technical Analysis of the Repository:
            {json.dumps(repo_analysis, indent=2)}

            CREATIVE DIRECTION from the previous analysis:
            - Metaphorical theme to develop: {metaphor_theme}
            - Visual atmosphere/vibe: {suggested_vibe}
            - Suggested music genre: {suggested_genre}
            """

            if free_form:
                creative_contract = """
                CREATIVE FREEDOM MODE:
                - Choose a linear, non-linear, circular, or fragmented narrative structure.
                - Write 2-8 scene seeds. Beats are optional and may be unconventional.
                - Use the repository as inspiration rather than a scene-by-scene checklist.
                - Include 1-4 symbol mappings only when they strengthen the film; each rationale is optional.
                - Prefer a distinctive cinematic idea over literal visualizations of code.
                """
            else:
                creative_contract = """
                GROUNDED STORY MODE:
                - Create a symbol mapping for every architecture component.
                - Explain why every symbol maps to its corresponding technical behavior.
                - Write 2-8 scene seeds that start with a 'cold start' beat and conclude with 'harmony'.
                - Keep every major visual grounded in a real repository capability.
                """

            prompt += f"""
            YOUR TASK — Create a Creative Brief:
            {creative_contract}

            Each scene seed must include a 1-indexed scene_number and a 1-2 sentence visual_seed.
            Use dramatic_beat when it improves clarity.

            Write ONE definitive soundtrack description that fits the entire film. Build on
            the suggested genre: "{suggested_genre}". Describe a cinematic narration voice
            with enough dramatic range for mystery, tension, and resolution.

            Return a strict JSON object.
            """

            response = self.client.models.generate_content(
                model='gemini-3.5-flash',
                contents=prompt,
                config=types.GenerateContentConfig(
                    response_mime_type="application/json",
                    response_schema=CreativeBriefSchema,
                ),
            )

            # Prefer SDK-parsed object
            if hasattr(response, 'parsed') and response.parsed is not None:
                parsed = response.parsed
                return {
                    "title": parsed.title,
                    "logline": parsed.logline,
                    "symbol_map": [
                        {"technical": s.technical, "symbol": s.symbol, "why": s.why}
                        for s in parsed.symbol_map
                    ],
                    "scene_arc": [
                        {"scene_number": s.scene_number, "dramatic_beat": s.dramatic_beat, "visual_seed": s.visual_seed}
                        for s in parsed.scene_arc
                    ],
                    "tone": parsed.tone,
                    "visual_anchors": parsed.visual_anchors,
                    "music_direction": parsed.music_direction,
                    "narration_voice": parsed.narration_voice,
                }

            # Fallback: robust text parser
            return robust_parse_json(response.text)

        except Exception as e:
            raise RuntimeError(f"[PromptArchitect] Creative brief generation failed: {e}")
