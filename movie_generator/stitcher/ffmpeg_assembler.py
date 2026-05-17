import os
import subprocess
import requests
import tempfile

class FFmpegAssembler:
    def __init__(self, ffmpeg_path: str = "ffmpeg"):
        self.ffmpeg_path = ffmpeg_path

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

    def stitch_movie(self, storyboard: dict, output_filepath: str) -> dict:
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
        assets_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "assets"))
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
