# Movie Generator

## Setup

From the project directory, install the declared runtime dependencies into the
local virtual environment:

```powershell
& ".\.venv\Scripts\python.exe" -m pip install -r requirements.txt
```

Install FFmpeg and make it available on `PATH`. It is required by Pydub for
audio mixing and by the movie assembler for video output.

Start the application from the repository parent directory:

```powershell
cd "c:\Users\ninic\project\hermes agent"
$env:GEMINI_API_KEY = "your-key-here"
& ".\movie_generator\.venv\Scripts\python.exe" -m uvicorn movie_generator.server:app --host 0.0.0.0 --port 8000
```

Open `http://127.0.0.1:8000` in your browser. Do not run `server.py` from
inside the `movie_generator` directory because its package imports require the
repository parent directory.

   [GitHub Repo]
         │
         ▼
  ┌───────────────┐
  │  GEMINI OMNI  │  <-- 1. Analyzes code, generates a cohesive storyboard &
  └───────┬───────┘         detailed visual prompts with strict style guidelines.
         │
         ├───► [Style Guide / Theme Seed]
         ▼
  ┌───────────────┐
  │  IMAGE GEN    │  <-- 2. Generates beautiful, styled keyframes (using Flux or Imagen)
  └───────┬───────┘         ensuring visual consistency across the entire video.
         │
         ▼
  ┌───────────────┐
  │ VIDEO / ZOOM  │  <-- 3. Converts keyframes to motion (using a fast Image-to-Video API
  └───────────────┘         like Luma/Runway, OR programmatically via Ken Burns/zoom effects).

## Creative Freedom Mode (`free_form`)

The pipeline supports an optional `free_form` flag that gives the creative
agents more room for abstract, non-linear, and semantically richer output.

### What changes when `free_form=True`

- **PromptArchitect** supports non-linear structures, optional scene beats,
  selective symbolic grounding, and 2-8 scene arcs.
- **StoryboardDirector** may transform or omit supplied metaphors and treats
  `creative_rationale` as optional, while retaining renderable visual, narration,
  timing, and audio fields.
- **Bounded output**: both modes enforce 2-8 scenes so image, speech, and video
  generation remain reliable.

### Usage

Pass the flag through the pipeline (it propagates to both sub‑agents):

```python
pipeline = AgentPipeline()  # or AgentPipeline(free_form=True) for a default
result = pipeline.run(
    repo_path=".",
    free_form=True,          # relax constraints for this run
)
```

You can also set the flag per agent:

```python
from movie_generator.agents.prompt_architect import PromptArchitect
from movie_generator.agents.storyboard_director import StoryboardDirector

architect = PromptArchitect(free_form=True)
director = StoryboardDirector(free_form=True)
```

Strict mode (default `free_form=False`) preserves the original deterministic
behaviour for backward compatibility.

## Offline Validation

Run the no-network mode and audio checks from the project directory:

```powershell
& ".\.venv\Scripts\python.exe" -m unittest discover -s tests -v
```

The suite verifies audio preference handling, no-speech behavior, 2-8 scene
boundaries, and that music is ducked only while narration is audible.
