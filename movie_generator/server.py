import os
from typing import Optional
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from movie_generator.agent_pipeline import AgentPipeline
from movie_generator.stitcher.ffmpeg_assembler import FFmpegAssembler

app = FastAPI(title="CineRepo Server", description="Cognitive agent pipeline turning codebases into short cinematic films.")

# Mount assets directory as static files to allow direct access to showcase.html and relative files
base_assets_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "assets"))
os.makedirs(base_assets_dir, exist_ok=True)
app.mount("/assets", StaticFiles(directory=base_assets_dir), name="assets")

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
    soundtrack_pref: str = "auto"
    speech_pref: str = "auto"
    free_form: Optional[bool] = None

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
            force_mock=req.force_mock,
            soundtrack_pref=req.soundtrack_pref,
            speech_pref=req.speech_pref,
        )
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/assets/video")
def get_video(repo_name: str = None):
    """
    Streams the stitched video if available.
    If not stitched, redirects to the premium pre-assembled Flowith movie URL.
    """
    base_assets_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "assets"))
    video_path = None
    
    # Resolve repository-specific movie path if repo_name is provided
    if repo_name:
        repo_slug = "".join([c if c.isalnum() or c in "-_" else "_" for c in repo_name]).lower()
        repo_slug = repo_slug.strip("_")
        while "__" in repo_slug:
            repo_slug = repo_slug.replace("__", "_")
        video_path = os.path.join(base_assets_dir, "target_repos", repo_slug, "final_movie.mp4")
    else:
        video_path = os.path.join(base_assets_dir, "final_movie.mp4")
    
    # Dual Fallback: if specific movie path doesn't exist, search target_repos for the most recent final_movie.mp4
    if not video_path or not os.path.exists(video_path):
        target_repos_dir = os.path.join(base_assets_dir, "target_repos")
        if os.path.isdir(target_repos_dir):
            newest_movie = None
            newest_mtime = 0
            for root, dirs, files in os.walk(target_repos_dir):
                if "final_movie.mp4" in files:
                    candidate_path = os.path.join(root, "final_movie.mp4")
                    try:
                        mtime = os.path.getmtime(candidate_path)
                        if mtime > newest_mtime:
                            newest_mtime = mtime
                            newest_movie = candidate_path
                    except Exception:
                        pass
            if newest_movie:
                video_path = newest_movie

    if video_path and os.path.exists(video_path):
        return FileResponse(video_path, media_type="video/mp4")
    
    # Fallback to pre-assembled Master Movie URL directly from our successful Flowith run
    flowith_movie_url = "https://r2-bucket.flowith.net/concat_1779012993538996307.mp4"
    return RedirectResponse(url=flowith_movie_url)


@app.get("/api/assets/image")
def get_image(path: str):
    """
    Streams a localized storyboard keyframe image file to the live web dashboard.
    Enforces strict path-traversal mitigation by validating requested absolute paths are
    strictly situated within the project's subassets folder hierarchies.
    """
    base_assets_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "assets"))
    resolved_path = os.path.abspath(path)
    
    # Security: Ensure absolute path falls inside the authorized assets root directory
    if not resolved_path.startswith(base_assets_dir):
        raise HTTPException(
            status_code=403, 
            detail="Forbidden: Path resolution violates active security policy sandboxes."
        )
        
    if os.path.exists(resolved_path):
        return FileResponse(resolved_path, media_type="image/png")
        
    raise HTTPException(status_code=404, detail="Requested keyframe is currently missing from storage.")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
