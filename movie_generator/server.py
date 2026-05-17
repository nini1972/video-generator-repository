import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, RedirectResponse
from pydantic import BaseModel
from movie_generator.agent_pipeline import AgentPipeline
from movie_generator.stitcher.ffmpeg_assembler import FFmpegAssembler

app = FastAPI(title="CineRepo Server", description="Cognitive agent pipeline turning codebases into short cinematic films.")

# Lightweight singleton for status checks — avoids constructing genai.Client on every poll
_ffmpeg_checker = FFmpegAssembler()

# Enable CORS for frontend dashboard communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class RunPipelineRequest(BaseModel):
    repo_path: str = "."
    gemini_api_key: str = ""
    force_mock: bool = False

@app.get("/")
def read_root():
    index_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "index.html"))
    if os.path.exists(index_path):
        return FileResponse(index_path)
    raise HTTPException(status_code=404, detail="Dashboard index.html not found.")


@app.get("/api/status")
def get_status():
    return {
        "status": "online",
        "ffmpeg_available": _ffmpeg_checker.is_ffmpeg_available(),
        "gemini_configured": "GEMINI_API_KEY" in os.environ and os.environ["GEMINI_API_KEY"].strip() != ""
    }

@app.post("/api/pipeline/run")
def run_pipeline(req: RunPipelineRequest):
    try:
        pipeline = AgentPipeline(
            gemini_api_key=req.gemini_api_key if req.gemini_api_key else None
        )
        # Use workspace path if repo_path is default or empty
        target_path = req.repo_path
        if not target_path or target_path == ".":
            target_path = os.getcwd()
            
        result = pipeline.run(
            repo_path=target_path,
            output_movie_filename="final_movie.mp4",
            force_mock=req.force_mock
        )
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/assets/video")
def get_video():
    """
    Streams the stitched video if available.
    If not stitched, redirects to the premium pre-assembled Flowith movie URL.
    """
    assets_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "assets"))
    video_path = os.path.join(assets_dir, "final_movie.mp4")
    
    if os.path.exists(video_path):
        return FileResponse(video_path, media_type="video/mp4")
    
    # Fallback to pre-assembled Master Movie URL directly from our successful Flowith run
    flowith_movie_url = "https://r2-bucket.flowith.net/concat_1779012993538996307.mp4"
    return RedirectResponse(url=flowith_movie_url)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
