import os
import json
import time
from movie_generator.agents.repo_investigator import RepoInvestigator
from movie_generator.agents.narrative_architect import NarrativeArchitect
from movie_generator.agents.storyboard_director import StoryboardDirector
from movie_generator.stitcher.ffmpeg_assembler import FFmpegAssembler


class AgentPipeline:
    def __init__(self, gemini_api_key: str = None, ffmpeg_path: str = "ffmpeg"):
        # IMPORTANT: Set the env var BEFORE constructing agents so their
        # genai.Client() picks up the key from the environment.
        # We write to both GEMINI_API_KEY and GOOGLE_API_KEY because the SDK
        # warns and prefers GOOGLE_API_KEY when both are present.
        if gemini_api_key:
            os.environ["GEMINI_API_KEY"] = gemini_api_key
            os.environ["GOOGLE_API_KEY"] = gemini_api_key

        self.investigator = RepoInvestigator()
        self.architect = NarrativeArchitect()
        self.director = StoryboardDirector()
        self.stitcher = FFmpegAssembler(ffmpeg_path=ffmpeg_path)

    def run(self, repo_path: str, output_movie_filename: str = "master_movie.mp4", force_mock: bool = False) -> dict:
        """
        Runs the complete end-to-end movie generation agent workflow:
        RepoInvestigator -> NarrativeArchitect -> StoryboardDirector -> FFmpegAssembler.

        Errors from each stage are caught, logged to pipeline_logs, and the stage
        gracefully degrades to demo data so the UI always receives a usable result.
        """
        pipeline_log = []
        pipeline_log.append("Initializing CineRepo Agent Pipeline...")

        api_key_set = (
            (os.environ.get("GEMINI_API_KEY", "").strip() != "") or
            (os.environ.get("GOOGLE_API_KEY", "").strip() != "")
        )
        use_mock = force_mock or not api_key_set

        if force_mock:
            pipeline_log.append("Force Demo Mode enabled — using premium Flowith cached assets.")
        elif not api_key_set:
            pipeline_log.append("No Gemini API Key detected. Booting in Demo Mode (NousResearch/hermes-agent showcase).")
        else:
            pipeline_log.append(f"Gemini API Key detected. Running live multi-agent cognitive pipeline on: '{repo_path}'")

        # ── Stage 1: Repo Analysis ─────────────────────────────────────────────
        pipeline_log.append("[STAGE 1] Launching RepoInvestigator Agent...")
        t0 = time.time()
        try:
            analysis = self.investigator.analyze(repo_path, mock_mode=use_mock)
            pipeline_log.append(
                f"RepoInvestigator completed in {time.time() - t0:.2f}s. "
                f"Project identified: '{analysis.get('repo_name', 'Unknown')}'"
            )
        except RuntimeError as e:
            pipeline_log.append(f"[STAGE 1 ERROR] {e}")
            pipeline_log.append("Stage 1 degraded to demo data — fix the error above to enable real analysis.")
            analysis = self.investigator.analyze(repo_path, mock_mode=True)

        # ── Stage 2: Screenplay Generation ────────────────────────────────────
        pipeline_log.append("[STAGE 2] Launching NarrativeArchitect Agent...")
        t1 = time.time()
        try:
            screenplay = self.architect.write_screenplay(analysis, mock_mode=use_mock)
            pipeline_log.append(
                f"NarrativeArchitect completed in {time.time() - t1:.2f}s. "
                f"Screenplay: '{screenplay.get('title', 'Untitled')}'"
            )
        except RuntimeError as e:
            pipeline_log.append(f"[STAGE 2 ERROR] {e}")
            pipeline_log.append("Stage 2 degraded to demo screenplay.")
            screenplay = self.architect.write_screenplay(analysis, mock_mode=True)

        # ── Stage 3: Storyboard Prompting ──────────────────────────────────────
        pipeline_log.append("[STAGE 3] Launching StoryboardDirector Agent...")
        t2 = time.time()
        try:
            storyboard = self.director.direct(screenplay, mock_mode=use_mock)
            scene_count = len(storyboard.get("storyboards", []))
            pipeline_log.append(
                f"StoryboardDirector completed in {time.time() - t2:.2f}s. "
                f"Storyboard populated with {scene_count} scenes."
            )
        except RuntimeError as e:
            pipeline_log.append(f"[STAGE 3 ERROR] {e}")
            pipeline_log.append("Stage 3 degraded to demo storyboard.")
            storyboard = self.director.direct(screenplay, mock_mode=True)

        # ── Stage 4: Movie Stitching & Assembly ────────────────────────────────
        pipeline_log.append("[STAGE 4] Launching ProductionStitcher & FFmpeg Engine...")
        t3 = time.time()

        assets_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "assets"))
        os.makedirs(assets_dir, exist_ok=True)
        movie_filepath = os.path.join(assets_dir, output_movie_filename)

        master_bundle = {
            "title": screenplay.get("title", "Untitled Allegory"),
            "logline": screenplay.get("logline"),
            "metaphors": screenplay.get("metaphors", []),
            "characters": screenplay.get("characters", []),
            "aesthetic_style": storyboard.get("aesthetic_style"),
            "scenes": storyboard.get("storyboards", []),
            "master_music_url": storyboard.get("master_music_url"),
            "master_speech_url": storyboard.get("master_speech_url"),
            "master_concat_video_url": storyboard.get("master_concat_video_url")
        }

        stitch_result = self.stitcher.stitch_movie(master_bundle, movie_filepath)
        pipeline_log.append(f"ProductionStitcher completed in {time.time() - t3:.2f}s.")

        for st_log in stitch_result.get("logs", []):
            pipeline_log.append(f"  > {st_log}")

        # ── Final Response ─────────────────────────────────────────────────────
        return {
            "success": True,
            "pipeline_logs": pipeline_log,
            "analysis": analysis,
            "screenplay": screenplay,
            "storyboard": storyboard,
            "stitch_result": {
                "success": stitch_result.get("success"),
                "output_movie": output_movie_filename,
                "command_executed": stitch_result.get("command_executed"),
                "ffmpeg_found": self.stitcher.is_ffmpeg_available()
            }
        }


if __name__ == "__main__":
    # Quick test — runs demo mode without requiring an API key
    pipeline = AgentPipeline()
    res = pipeline.run(repo_path=".", force_mock=True)
    print("\n--- Pipeline Logs ---")
    for log in res["pipeline_logs"]:
        print(log)
