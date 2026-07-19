import os
import time
from typing import Optional
from movie_generator.agents.repo_investigator import RepoInvestigator
from movie_generator.agents.prompt_architect import PromptArchitect
from movie_generator.agents.storyboard_director import StoryboardDirector
from movie_generator.audio.mixer import AudioMixer
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
        else:
            # Overwrite user's static system-wide GOOGLE_API_KEY if they set GEMINI_API_KEY in the shell environment.
            # This prevents key masking where the SDK implicitly prefers a stale/free system-wide GOOGLE_API_KEY.
            env_key = os.environ.get("GEMINI_API_KEY")
            if env_key:
                os.environ["GOOGLE_API_KEY"] = env_key

        self.investigator = RepoInvestigator()
        self.prompt_architect = PromptArchitect()
        self.director = StoryboardDirector()
        self.mixer = AudioMixer()
        self.stitcher = FFmpegAssembler(ffmpeg_path=ffmpeg_path)

    def run(self, repo_path: str, output_movie_filename: str = "master_movie.mp4", force_mock: bool = False, soundtrack_pref: str = "auto", speech_pref: str = "auto") -> dict:
        """
        Runs the complete end-to-end movie generation agent workflow:
        RepoInvestigator -> PromptArchitect -> StoryboardDirector -> FFmpegAssembler.

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

        pipeline_log.append(
            "Creative mode: free-form."
        )
        if use_mock:
            pipeline_log.append(
                "Demo output is deterministic: it always uses the cached Hermes brief and "
                "four-scene storyboard. Auto-Direct audio therefore resolves to its cached defaults."
            )

        # ── Stage 1: Repo Analysis ─────────────────────────────────────────────
        pipeline_log.append("[STAGE 1] Launching RepoInvestigator Agent...")
        t0 = time.time()
        try:
            analysis = self.investigator.analyze(
                repo_path,
                mock_mode=use_mock,
            )
            pipeline_log.append(
                f"RepoInvestigator completed in {time.time() - t0:.2f}s. "
                f"Project identified: '{analysis.get('repo_name', 'Unknown')}'"
            )
        except RuntimeError as e:
            pipeline_log.append(f"[STAGE 1 ERROR] {e}")
            pipeline_log.append("Stage 1 degraded to cached demo data — subsequent output may be deterministic.")
            analysis = self.investigator.analyze(
                repo_path,
                mock_mode=True,
            )

        # ── Stage 2: Creative Brief Generation ─────────────────────────────────
        pipeline_log.append("[STAGE 2] Launching PromptArchitect Agent...")
        t1 = time.time()
        try:
            creative_brief = self.prompt_architect.craft_brief(
                analysis, mock_mode=use_mock
            )
            symbol_count = len(creative_brief.get("symbol_map", []))
            scene_count = len(creative_brief.get("scene_arc", []))
            pipeline_log.append(
                f"PromptArchitect completed in {time.time() - t1:.2f}s. "
                f"Brief: '{creative_brief.get('title', 'Untitled')}' ({symbol_count} symbols mapped, {scene_count} scenes)."
            )
        except RuntimeError as e:
            pipeline_log.append(f"[STAGE 2 ERROR] {e}")
            pipeline_log.append("Stage 2 degraded to cached demo creative brief — it contains four scene seeds.")
            creative_brief = self.prompt_architect.craft_brief(
                analysis, mock_mode=True
            )

        # Generate a slug from the repository name to namespace assets
        repo_name = analysis.get("repo_name", "unknown_repo")
        # Keep alphanumeric characters and convert spaces/slashes to underscores
        repo_slug = "".join([c if c.isalnum() or c in "-_" else "_" for c in repo_name]).lower()
        repo_slug = repo_slug.strip("_")
        while "__" in repo_slug:
            repo_slug = repo_slug.replace("__", "_")

        # ── Stage 3: Storyboard Prompting ──────────────────────────────────────
        pipeline_log.append("[STAGE 3] Launching StoryboardDirector Agent...")
        t2 = time.time()
        try:
            storyboard = self.director.direct(
                creative_brief, 
                mock_mode=use_mock, 
                repo_slug=repo_slug,
                soundtrack_pref=soundtrack_pref,
                speech_pref=speech_pref,
            )
            scene_count = len(storyboard.get("storyboards", []))
            pipeline_log.append(
                f"StoryboardDirector completed in {time.time() - t2:.2f}s. "
                f"Storyboard populated with {scene_count} scenes (using namespace cache: '{repo_slug}')."
            )
        except RuntimeError as e:
            pipeline_log.append(f"[STAGE 3 ERROR] {e}")
            pipeline_log.append("Stage 3 degraded to cached demo storyboard — Auto-Direct uses instrumental music and full narration.")
            storyboard = self.director.direct(
                creative_brief, 
                mock_mode=True, 
                repo_slug=None,
                soundtrack_pref=soundtrack_pref,
                speech_pref=speech_pref,
            )

        # ── Stage 3.5: Audio Mixing ────────────────────────────────────────────
        pipeline_log.append("[STAGE 3.5] Launching AudioMixer...")
        t_mix = time.time()

        base_assets_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "assets"))
        if repo_slug:
            assets_dir = os.path.join(base_assets_dir, "target_repos", repo_slug)
        else:
            assets_dir = base_assets_dir
            
        os.makedirs(assets_dir, exist_ok=True)
        movie_filepath = os.path.join(assets_dir, output_movie_filename)

        scenes = storyboard.get("storyboards", [])
        audio_dir_opts = storyboard.get("audio_direction", {}) or {}
        speech_mode = audio_dir_opts.get("speech_mode", "full_narration")
        soundtrack_mode = audio_dir_opts.get("soundtrack_mode", "instrumental_only")

        scene_speech_paths = [s.get("local_speech_path") for s in scenes]
        scene_durations = [s.get("duration_seconds", 8.0) for s in scenes]
        local_music_path = storyboard.get("local_music_path")

        local_mixed_audio_path = self.mixer.mix_master_audio(
            scene_speech_paths=scene_speech_paths,
            scene_durations=scene_durations,
            soundtrack_path=local_music_path,
            speech_mode=speech_mode,
            soundtrack_mode=soundtrack_mode,
            output_dir=assets_dir,
        )
        pipeline_log.append(f"AudioMixer completed in {time.time() - t_mix:.2f}s.")
        if local_mixed_audio_path:
            pipeline_log.append(f"  Master audio: {os.path.basename(local_mixed_audio_path)}")
        else:
            pipeline_log.append("  No mixed audio produced (silent mode or generation skipped).")

        # ── Stage 4: Movie Stitching & Assembly ────────────────────────────────
        pipeline_log.append("[STAGE 4] Launching ProductionStitcher & FFmpeg Engine...")
        t3 = time.time()

        master_bundle = {
            "title": creative_brief.get("title", "Untitled Allegory"),
            "logline": creative_brief.get("logline"),
            "symbol_map": creative_brief.get("symbol_map", []),
            "aesthetic_style": storyboard.get("aesthetic_style"),
            "audio_direction": storyboard.get("audio_direction"),
            "scenes": storyboard.get("storyboards", []),
            "master_music_url": storyboard.get("master_music_url"),
            "master_speech_url": storyboard.get("master_speech_url"),
            "master_concat_video_url": storyboard.get("master_concat_video_url"),
            "local_mixed_audio_path": local_mixed_audio_path,
        }

        stitch_result = self.stitcher.stitch_movie(master_bundle, movie_filepath, repo_slug=repo_slug)
        pipeline_log.append(f"ProductionStitcher completed in {time.time() - t3:.2f}s.")

        for st_log in stitch_result.get("logs", []):
            pipeline_log.append(f"  > {st_log}")

        # ── Final Response ─────────────────────────────────────────────────────
        return {
            "success": True,
            "pipeline_logs": pipeline_log,
            "analysis": analysis,
            "creative_brief": creative_brief,
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
