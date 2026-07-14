import os
import shutil
import subprocess
import requests
import tempfile


def _locate_ffmpeg() -> str:
    """
    Locates the ffmpeg executable even when the server process inherited a
    stale PATH (e.g. started before a winget install updated PATH).

    Search order:
      1. shutil.which() against the current process PATH
      2. Re-read PATH from the Windows registry (system + user) and search again
      3. Known winget / Chocolatey / common install locations
    """
    # 1. Fast path — already on current PATH
    found = shutil.which("ffmpeg")
    if found:
        return found

    # 2. Read live PATH from Windows registry so we work even if PATH is stale
    try:
        import winreg
        paths = []
        for hive, subkey in [
            (winreg.HKEY_LOCAL_MACHINE,
             r"SYSTEM\CurrentControlSet\Control\Session Manager\Environment"),
            (winreg.HKEY_CURRENT_USER, r"Environment"),
        ]:
            try:
                with winreg.OpenKey(hive, subkey) as key:
                    val, _ = winreg.QueryValueEx(key, "Path")
                    paths.append(val)
            except FileNotFoundError:
                pass
        combined = os.pathsep.join(paths)
        found = shutil.which("ffmpeg", path=combined)
        if found:
            return found
        # Also walk the directories manually for ffmpeg.exe
        for directory in combined.split(os.pathsep):
            candidate = os.path.join(directory.strip(), "ffmpeg.exe")
            if os.path.isfile(candidate):
                return candidate
    except Exception:
        pass

    # 3. Hardcoded fallback paths (winget, Chocolatey, Scoop, system)
    fallbacks = [
        # winget Gyan.FFmpeg pattern (version-agnostic glob not possible, check known)
        os.path.expandvars(
            r"%LOCALAPPDATA%\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe"
        ),
        r"C:\ProgramData\chocolatey\bin\ffmpeg.exe",
        r"C:\tools\ffmpeg\bin\ffmpeg.exe",
        r"C:\Program Files\ffmpeg\bin\ffmpeg.exe",
        r"C:\Program Files (x86)\ffmpeg\bin\ffmpeg.exe",
        os.path.expanduser(r"~\scoop\apps\ffmpeg\current\bin\ffmpeg.exe"),
    ]
    for path in fallbacks:
        if os.path.isdir(path):
            # Walk one level into winget package dir to find versioned sub-folder
            try:
                for entry in os.scandir(path):
                    candidate = os.path.join(entry.path, "bin", "ffmpeg.exe")
                    if os.path.isfile(candidate):
                        return candidate
            except Exception:
                pass
        elif os.path.isfile(path):
            return path

    return "ffmpeg"  # last resort — let subprocess raise the error naturally


class FFmpegAssembler:
    def __init__(self, ffmpeg_path: str = "ffmpeg"):
        # Auto-locate ffmpeg if only the bare name was supplied
        self.ffmpeg_path = _locate_ffmpeg() if ffmpeg_path == "ffmpeg" else ffmpeg_path

    def is_ffmpeg_available(self) -> bool:
        try:
            subprocess.run([self.ffmpeg_path, "-version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
            return True
        except Exception:
            return False

    def download_file(self, url: str, dest_path: str) -> bool:
        """Helper to download mock or remote assets securely."""
        try:
            response = requests.get(url, stream=True, timeout=30)
            if response.status_code == 200:
                with open(dest_path, 'wb') as f:
                    for chunk in response.iter_content(chunk_size=8192):
                        f.write(chunk)
                return True
        except Exception as e:
            print(f"Failed to download {url}: {e}")
        return False

    def _create_ken_burns_clip(
        self, image_path: str, duration: float, output_path: str
    ) -> bool:
        """
        Renders a slow zoom-in (Ken Burns) video clip from a still image.
        Output: 1920x1080, libx264, 25 fps, yuv420p.
        """
        frames = max(1, int(duration * 25))
        zoom_filter = (
            "scale=3840:-1,"
            f"zoompan=z='min(zoom+0.0008,1.5)':"
            "x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':"
            f"d={frames}:fps=25:s=1920x1080"
        )
        cmd = [
            self.ffmpeg_path, "-y",
            "-loop", "1", "-framerate", "25",
            "-i", image_path,
            "-vf", zoom_filter,
            "-c:v", "libx264",
            "-t", str(duration),
            "-pix_fmt", "yuv420p",
            output_path,
        ]
        try:
            result = subprocess.run(cmd, capture_output=True, timeout=180)
            return result.returncode == 0
        except Exception:
            return False

    def _concatenate_video_clips(
        self, clip_paths: list, output_path: str
    ) -> bool:
        """Concatenates a list of .mp4 clips into a single file."""
        concat_list = output_path + ".concat_list.txt"
        try:
            with open(concat_list, "w", encoding="utf-8") as f:
                for p in clip_paths:
                    # ffmpeg concat demuxer requires forward slashes
                    safe_p = p.replace("\\", "/")
                    f.write(f"file '{safe_p}'\n")
            cmd = [
                self.ffmpeg_path, "-y",
                "-f", "concat", "-safe", "0",
                "-i", concat_list,
                "-c", "copy",
                output_path,
            ]
            result = subprocess.run(cmd, capture_output=True, timeout=300)
            return result.returncode == 0
        except Exception:
            return False
        finally:
            if os.path.exists(concat_list):
                os.unlink(concat_list)

    def stitch_movie(self, storyboard: dict, output_filepath: str, repo_slug: str = None) -> dict:
        """
        Processes individual storyboard segments, downloads resources,
        and mixes audio tracks (voiceover + background music at -18dB) with video,
        compiling them into a final .mp4 file.
        """
        logs = []
        logs.append(f"Starting compilation for movie: '{storyboard.get('title', 'Untitled Allegory')}'")

        # 1. Check if FFmpeg is available
        ffmpeg_ok = self.is_ffmpeg_available()
        logs.append(f"Verifying FFmpeg executable: {'FOUND' if ffmpeg_ok else 'NOT FOUND'}")
        
        # 2. Extract asset urls
        music_url = storyboard.get("master_music_url")
        speech_url = storyboard.get("master_speech_url")
        concat_video_url = storyboard.get("master_concat_video_url")
        
        # Set up working directory inside project root to store outputs cleanly
        base_assets_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "assets"))
        if repo_slug:
            assets_dir = os.path.join(base_assets_dir, "target_repos", repo_slug)
        else:
            assets_dir = base_assets_dir
            
        os.makedirs(assets_dir, exist_ok=True)
        
        local_music = os.path.join(assets_dir, "music.mp3")
        local_speech = os.path.join(assets_dir, "narration.mp3")
        local_concat_video = os.path.join(assets_dir, "concat_visuals.mp4")

        # 3. Download/Verify cached assets
        if music_url:
            logs.append(f"Caching soundtrack: {music_url}")
            if not os.path.exists(local_music):
                success = self.download_file(music_url, local_music)
                logs.append(f"Soundtrack download status: {'SUCCESS' if success else 'FAILED'}")
            else:
                logs.append("Soundtrack already cached locally.")

        if speech_url:
            logs.append(f"Caching speech voiceover: {speech_url}")
            if not os.path.exists(local_speech):
                success = self.download_file(speech_url, local_speech)
                logs.append(f"Speech download status: {'SUCCESS' if success else 'FAILED'}")
            else:
                logs.append("Speech voiceover already cached locally.")

        if concat_video_url:
            logs.append(f"Caching master video reels: {concat_video_url}")
            if not os.path.exists(local_concat_video):
                success = self.download_file(concat_video_url, local_concat_video)
                logs.append(f"Master video reels download status: {'SUCCESS' if success else 'FAILED'}")
            else:
                logs.append("Master video reels already cached locally.")

        # ── Ken Burns path: build video from AI-generated scene images ─────────
        scenes = storyboard.get("scenes", []) or storyboard.get("storyboards", [])
        images_ready = [
            s for s in scenes
            if s.get("local_image_path") and os.path.exists(s["local_image_path"])
        ]
        if ffmpeg_ok and len(images_ready) == len(scenes) and len(scenes) > 0:
            logs.append(
                f"Building personalised Ken Burns video from {len(scenes)} generated images..."
            )
            clip_paths = []
            all_clips_ok = True
            for scene in scenes:
                img_file = scene["local_image_path"]
                img_name = os.path.splitext(os.path.basename(img_file))[0]
                clip_out = os.path.join(
                    assets_dir, f"{img_name}_clip.mp4"
                )
                
                if os.path.exists(clip_out):
                    logs.append(f"  Using cached scene {scene.get('scene_number')} clip: {clip_out}")
                    clip_paths.append(clip_out)
                    continue

                logs.append(f"  Rendering scene {scene.get('scene_number')} clip...")
                ok = self._create_ken_burns_clip(
                    img_file,
                    scene.get("duration_seconds", 8.0),
                    clip_out,
                )
                if ok:
                    clip_paths.append(clip_out)
                else:
                    logs.append(
                        f"  Scene {scene.get('scene_number')} clip failed — "
                        "falling back to cached video."
                    )
                    all_clips_ok = False
                    break

            if all_clips_ok:
                kb_concat = os.path.join(assets_dir, "ken_burns_concat.mp4")
                if self._concatenate_video_clips(clip_paths, kb_concat):
                    local_concat_video = kb_concat
                    logs.append("Ken Burns personalised video assembled successfully!")
                else:
                    logs.append("Concatenation failed — falling back to cached video.")
        # ──────────────────────────────────────────────────────────────────────

        # 4. Synthesize FFmpeg Command
        # This mixes narration (input 1) and background music (input 2, volume lowered by -18dB to ensure crisp dialog)
        # overlaying it directly on the compiled visual video stream (input 0).
        ffmpeg_cmd = [
            self.ffmpeg_path, "-y",
            "-i", local_concat_video,  # [0] Visuals (no audio)
            "-i", local_speech,        # [1] Narration Voiceover
            "-i", local_music,         # [2] Background Soundtrack
            "-filter_complex", 
            "[2:a]volume=0.15[bg]; [1:a][bg]amix=inputs=2:duration=longest[mixed_audio]",
            "-map", "0:v",             # Map video from [0]
            "-map", "[mixed_audio]",   # Map mixed audio track
            "-c:v", "copy",            # Copy video stream directly (super fast, no re-encoding!)
            "-c:a", "aac",             # Compress audio as standard ACC stream
            "-shortest",               # Stop recording when shortest stream ends (prevents infinite music trails)
            output_filepath
        ]

        cmd_string = " ".join(ffmpeg_cmd)
        logs.append(f"Generated FFmpeg Command:\n`{cmd_string}`")

        # 5. Run compilation if FFmpeg is available
        if ffmpeg_ok:
            try:
                logs.append("Executing program assembly in sub-process...")
                result = subprocess.run(ffmpeg_cmd, capture_output=True, text=True, check=True)
                logs.append("FFmpeg process completed successfully!")
                return {
                    "success": True,
                    "output_filepath": output_filepath,
                    "command_executed": cmd_string,
                    "logs": logs,
                    "stderr": result.stderr
                }
            except subprocess.CalledProcessError as e:
                logs.append(f"FFmpeg process failed with error code: {e.returncode}")
                logs.append(f"Error Message:\n{e.stderr}")
                return {
                    "success": False,
                    "output_filepath": None,
                    "command_executed": cmd_string,
                    "logs": logs,
                    "error": e.stderr
                }
        else:
            logs.append("Compilation Skipped: FFmpeg executable is not installed or added to the path in the local environment.")
            logs.append("Note: The server will serve the remote pre-assembled master video URL (concat_1779012993538996307.mp4) directly, ensuring a perfect full-cinema visual demonstration!")
            return {
                "success": False,
                "output_filepath": None,
                "command_executed": cmd_string,
                "logs": logs,
                "error": "FFmpeg not available in the system PATH"
            }
