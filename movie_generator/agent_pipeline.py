import os
import json
import time
from movie_generator.agents.repo_investigator import RepoInvestigator
from movie_generator.agents.narrative_architect import NarrativeArchitect
from movie_generator.agents.storyboard_director import StoryboardDirector
from movie_generator.stitcher.ffmpeg_assembler import FFmpegAssembler

class AgentPipeline:
    def __init__(self, gemini_api_key: str = None, ffmpeg_path: str = "ffmpeg"):
        # Configure API key in env if provided, else use existing env key
        if gemini_api_key:
            os.environ["GEMINI_API_KEY"] = gemini_api_key
            
        self.investigator = RepoInvestigator()
        self.architect = NarrativeArchitect()
        self.director = StoryboardDirector()
        self.stitcher = FFmpegAssembler(ffmpeg_path=ffmpeg_path)

    def run(self, repo_path: str, output_movie_filename: str = "master_movie.mp4", force_mock: bool = False) -> dict:
        """
        Runs the complete end-to-end movie generation agent workflow:
        RepoInvestigator -> NarrativeArchitect -> StoryboardDirector -> FFmpegAssembler.
        """
        pipeline_log = []
        pipeline_log.append("Initializing CineRepo Agent Pipeline...")
        
        # Check API Key status to notify user of dry-run vs real generation
        api_key_set = "GEMINI_API_KEY" in os.environ and os.environ["GEMINI_API_KEY"].strip() != ""
        use_mock = force_mock or not api_key_set
        
        if use_mock:
            pipeline_log.append("No Gemini API Key found or mock mode forced. Booting in 'High-Quality Mock Demo Mode' (Tending to NousResearch/hermes-agent)...")
        else:
            pipeline_log.append("Gemini API Key detected! Running live multi-agent cognitive pipeline...")

        # Stage 1: Repo Analysis
        pipeline_log.append("[STAGE 1] Launching RepoInvestigator Agent...")
        t0 = time.time()
        analysis = self.investigator.analyze(repo_path, mock_mode=use_mock)
        pipeline_log.append(f"RepoInvestigator completed in {time.time() - t0:.2f}s. Project Identified: {analysis.get('repo_name')}")

        # Stage 2: Screenplay Generation
        pipeline_log.append("[STAGE 2] Launching NarrativeArchitect Agent...")
        t1 = time.time()
        screenplay = self.architect.write_screenplay(analysis, mock_mode=use_mock)
        pipeline_log.append(f"NarrativeArchitect completed in {time.time() - t1:.2f}s. Metaphor Script Written: '{screenplay.get('title')}'")

        # Stage 3: Storyboard Prompting
        pipeline_log.append("[STAGE 3] Launching StoryboardDirector Agent...")
        t2 = time.time()
        storyboard = self.director.direct(screenplay, mock_mode=use_mock)
        pipeline_log.append(f"StoryboardDirector completed in {time.time() - t2:.2f}s. Storyboards populated with {len(storyboard.get('storyboards', []))} scenes.")

        # Stage 4: Movie Stitching & Assembly
        pipeline_log.append("[STAGE 4] Launching ProductionStitcher & FFmpeg Engine...")
        t3 = time.time()
        
        # Generate paths
        assets_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "assets"))
        os.makedirs(assets_dir, exist_ok=True)
        movie_filepath = os.path.join(assets_dir, output_movie_filename)
        
        # Build master JSON bundle
        master_bundle = {
            "title": screenplay.get("title", "The Gardener of Echoes"),
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

        # Assemble final response
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
    # Test execution
    pipeline = AgentPipeline()
    res = pipeline.run(repo_path=".", force_mock=True)
    print("\n--- Pipeline Logs ---")
    for log in res["pipeline_logs"]:
        print(log)
