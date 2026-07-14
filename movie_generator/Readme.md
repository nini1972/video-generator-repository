cd "c:\Users\ninic\project\hermes agent"
$env:GEMINI_API_KEY = "your-key-here"
python -m uvicorn movie_generator.server:app --host 0.0.0.0 --port 8000


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