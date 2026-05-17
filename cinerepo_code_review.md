# CineRepo Code Review & Recommendations

## 📋 Repository Structure

```
movie_generator/
├── __init__.py
├── agent_pipeline.py        # End-to-end orchestrator
├── server.py                # FastAPI server + root route
├── index.html               # Glassmorphic dashboard UI
├── agents/
│   ├── __init__.py
│   ├── repo_investigator.py     # Stage 1: Code analysis
│   ├── narrative_architect.py   # Stage 2: Screenplay writing
│   └── storyboard_director.py   # Stage 3: Visual direction
├── stitcher/
│   ├── __init__.py
│   └── ffmpeg_assembler.py      # Stage 4: Audio/video mixing
└── assets/
    ├── concat_visuals.mp4       # Pre-cached Flowith video (53 MB)
    ├── music.mp3                # Pre-cached soundtrack
    └── narration.mp3            # Pre-cached narration
```

---

## 🔴 Root Cause: Why the Pipeline Never Generates Its Own Analysis

This is the **core bug**. All three agent files share the same pattern — they check `mock_mode` first, then fall back to cached Hermes Agent data silently. When you run a different repo, the pipeline **always returns the Hermes mock** even with a valid API key. Here's the chain of failures:

### Issue 1 — `agent_pipeline.py`: `force_mock` defaults to `True` in the UI

```python
# agent_pipeline.py line 30
use_mock = force_mock or not api_key_set
```

In `index.html` line 795, the **Force Demo Mode checkbox is `checked` by default**:
```html
<input type="checkbox" id="forceMock" checked>
```

This means **every pipeline run is a mock by default** unless the user manually unchecks the box. Most users will never notice.

---

### Issue 2 — `repo_investigator.py`: Silent fallback hides real errors

```python
# Line 96-98
except Exception as e:
    print(f"Error during real repo analysis: {e}. Falling back to mock data.")
    return self.analyze(repo_path, mock_mode=True)   # ← Silent Hermes data returned
```

If the Gemini API key is wrong, the path is invalid, or the model returns bad JSON, the error is **swallowed silently** and the fixed Hermes analysis is returned without the caller knowing. The pipeline then continues generating a Hermes screenplay for a completely different repo.

---

### Issue 3 — `repo_investigator.py`: JSON parsing is fragile

```python
# Line 94
return json.loads(response.text)
```

Gemini with `response_mime_type="application/json"` can still return markdown-fenced JSON (` ```json ... ``` `). If it does, `json.loads()` throws and triggers the silent fallback to mock data.

---

### Issue 4 — `narrative_architect.py` & `storyboard_director.py`: Same silent fallback pattern

Both agents repeat the same silent exception swallowing:
```python
except Exception as e:
    print(f"Error in NarrativeArchitect: {e}. Falling back to mock...")
    return self.write_screenplay(repo_analysis, mock_mode=True)  # Hermes data again
```

Even if Stage 1 succeeds with real repo data, a failure in Stage 2 resets everything back to *The Gardener of Echoes*.

---

### Issue 5 — `storyboard_director.py`: Real mode returns no asset URLs

When `mock_mode=False` and Gemini generates a real storyboard, the output **does not include** `image_url`, `video_url`, `master_music_url`, `master_speech_url`, or `master_concat_video_url`. The prompt on line 73-81 doesn't ask for them.

This means the video player in the dashboard will be empty (or attempt to stream the fixed Flowith video regardless of which repo was analysed).

---

### Issue 6 — `server.py` & `agent_pipeline.py`: No error surfacing to the UI

The server wraps everything in a broad `try/except` that returns HTTP 500, but the frontend only logs `pipeline_logs`. Gemini API errors (e.g. quota exceeded, bad key) are never shown to the user in the terminal console panel.

---

## 🟡 Secondary Issues

| # | Location | Issue |
|---|----------|-------|
| 7 | `repo_investigator.py` L44 | `max_files = 15` is very low — most repos need 25-40 files to build a meaningful picture. Also, binary files (`.pyc`, images) are not explicitly excluded. |
| 8 | `repo_investigator.py` L57 | Only reads first **1500 chars** per file. For Python files this is often just imports, missing the actual logic. Should be ~3000-5000 chars. |
| 9 | `agent_pipeline.py` | No `__init__.py` entry to set `GEMINI_API_KEY` before the agents instantiate their clients. The key set via `os.environ` in `__init__` happens *after* `genai.Client()` is called in each agent's constructor. |
| 10 | `agent_pipeline.py` | Pipeline runs synchronously in the FastAPI request thread. For large repos, Gemini calls can take 30-60 seconds and block the server. |
| 11 | `assets/` | The `concat_visuals.mp4` (53 MB) is cached locally but is always used as the video — even for a different repo's output. There's no per-repo asset isolation. |
| 12 | `server.py` | `ffmpeg_assembler.py` is instantiated on every `/api/status` call (`pipeline = AgentPipeline()`), which triggers `genai.Client()` construction and environment reads unnecessarily. |

---

## ✅ Recommended Fixes (Prioritised)

### Fix 1 — Uncheck `forceMock` by default in the UI *(Quick win)*
```diff
- <input type="checkbox" id="forceMock" checked>
+ <input type="checkbox" id="forceMock">
```

### Fix 2 — Surface errors to the pipeline logs instead of swallowing them

In all three agents, replace the silent fallback with explicit error propagation:
```python
# In repo_investigator.py, narrative_architect.py, storyboard_director.py
except Exception as e:
    error_msg = f"[AGENT ERROR] {self.__class__.__name__} failed: {e}"
    print(error_msg)
    raise RuntimeError(error_msg)   # ← Let pipeline.py catch and surface it
```

Then in `agent_pipeline.py`, catch per-stage and add the error to `pipeline_log`:
```python
try:
    analysis = self.investigator.analyze(repo_path, mock_mode=use_mock)
except RuntimeError as e:
    pipeline_log.append(str(e))
    # Decide: fail fast OR fall back to mock with explicit notice
    pipeline_log.append("Falling back to demo data — check your API key and repo path.")
    analysis = self.investigator.analyze(repo_path, mock_mode=True)
```

### Fix 3 — Fix API key timing: set env var before constructing agents

```python
# agent_pipeline.py __init__
def __init__(self, gemini_api_key: str = None, ffmpeg_path: str = "ffmpeg"):
    if gemini_api_key:
        os.environ["GEMINI_API_KEY"] = gemini_api_key   # ← Must happen FIRST
    
    # Now construct agents — they'll pick up the key correctly
    self.investigator = RepoInvestigator()
    ...
```

This is already the structure in the code, but confirm each agent's constructor uses `os.environ.get("GEMINI_API_KEY")` lazily at call time — which they do via `genai.Client()`.

### Fix 4 — Robust JSON parsing with fence stripping

```python
# In all three agents — replace the bare json.loads call
import re

def _parse_json(self, text: str) -> dict:
    """Strip markdown fences if present, then parse JSON."""
    text = text.strip()
    match = re.search(r'```(?:json)?\s*([\s\S]+?)```', text)
    if match:
        text = match.group(1).strip()
    return json.loads(text)
```

### Fix 5 — Increase file scan coverage in `RepoInvestigator`

```python
max_files = 30          # Was 15
content = f.read(4000)  # Was 1500 chars
```

Also add a `README.md` priority pass — always read the README first as it provides the most context.

### Fix 6 — Add `master_music_url` / `master_speech_url` fallbacks in real storyboard mode

In `storyboard_director.py` real-mode output, add the Flowith URLs as fallbacks when no real generation has happened yet (until we integrate Fal.ai / ElevenLabs):
```python
result = json.loads(self._parse_json(response.text))
# Inject audio fallbacks until real TTS/music generation is wired in
result.setdefault("master_music_url", "https://v3b.fal.media/files/b/0a9a8cb8/K0cxAgb2F5nkl5PvR2r9C_output.mp3")
result.setdefault("master_speech_url", "https://v3b.fal.media/files/b/0a9a8cbc/NjDP_0GI1rwgTAYGRNJWu_speech.mp3")
result.setdefault("master_concat_video_url", "https://r2-bucket.flowith.net/concat_1779012993538996307.mp4")
return result
```

---

## 🔮 Longer-Term Improvements

| Improvement | Why |
|-------------|-----|
| **Async pipeline** (`asyncio` + `BackgroundTasks`) | Long Gemini calls block the server; use FastAPI `BackgroundTasks` and poll status via a job ID endpoint. |
| **GitHub URL support** | `RepoInvestigator` currently only reads local paths. Add `GitPython` cloning of a remote URL to `assets/repos/{hash}/`. |
| **Per-repo asset isolation** | Use a hash of the repo path as an `assets/{hash}/` subdirectory so multiple repos don't overwrite each other's cached videos. |
| **Real image/video generation** | Wire `storyboard_director.py` to call `fal.ai` or `Imagen 3` and populate `image_url`/`video_url` fields per scene. |
| **ElevenLabs / Chirp TTS** | Generate per-repo narration audio based on the actual screenplay text, replacing the fixed `narration.mp3`. |
| **Progress streaming (SSE)** | Replace the single blocking `POST /api/pipeline/run` with a Server-Sent Events stream so the dashboard shows real-time node updates during live generation. |

---

## Summary Priority Order

```
🔴 Critical (fix now — breaks real analysis):
  1. Uncheck forceMock default in index.html
  2. Surface errors — stop silent fallback to Hermes data
  3. Robust JSON parsing with fence stripping

🟡 Important (fix soon — degrades real output):
  4. Increase file scan coverage (max_files, content length)
  5. Add audio URL fallbacks to real storyboard output
  6. Fix status-check unnecessarily creating AgentPipeline

🟢 Future (architecture improvements):
  7. Async pipeline with background tasks
  8. GitHub URL cloning support
  9. Per-repo asset isolation
```
