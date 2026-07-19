import os
import subprocess
import tempfile
import shutil
from typing import List, Optional, cast
from pydantic import BaseModel
from google import genai
from google.genai import types
from movie_generator.agents.json_utils import robust_parse_json


# ── Output schema — forces Gemini to produce well-formed JSON ─────────────────
class AmbientProfile(BaseModel):
    metaphor_theme: str         
    suggested_vibe: str         
    suggested_music_genre: str  

class ArchitectureComponent(BaseModel):
    name: str
    purpose: str

class RepoAnalysisSchema(BaseModel):
    repo_name: str
    core_purpose: str
    architecture_components: List[ArchitectureComponent]
    technologies_used: List[str]
    ambient: AmbientProfile


class RepoInvestigator:
    client: Optional[genai.Client]

    def __init__(self, client: Optional[genai.Client] = None):
        if client:
            self.client = client
        else:
            api_key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
            self.client = genai.Client(api_key=api_key) if api_key else None

    def _get_mock_data(self) -> dict:
        """Returns the cached Hermes Agent analysis for demo/fallback use."""
        return {
            "repo_name": "NousResearch/hermes-agent",
            "core_purpose": "A self-improving, autonomous AI agent with persistent long-term memory, cross-session execution, and tool/skill generation.",
            "architecture_components": [
                {
                    "name": "SQLite FTS5 Memory System",
                    "purpose": "Provides full-text search across prior conversation logs, enabling cross-session recall and preventing amnesia."
                },
                {
                    "name": "Autonomous Skill Creation (agentskills.io)",
                    "purpose": "Dynamically builds, tests, and saves Markdown-based script templates that function as new reusable tools."
                },
                {
                    "name": "Parallel Sub-Agent Delegation",
                    "purpose": "Spawns isolated sub-agents via RPC commands to handle complex sub-workflows concurrently without cluttering the main conversation."
                },
                {
                    "name": "Multi-Model & Provider Support",
                    "purpose": "Decoupled from a single vendor, allowing direct connection to Portal, OpenRouter, Anthropic, or OpenAI."
                }
            ],
            "technologies_used": ["Python", "SQLite", "FTS5", "RPC", "Markdown Skills"],
            "ambient": {
                "metaphor_theme": "A weary crystalline floating core named Hermes tending to a digital greenhouse of glowing autonomous skills",
                "suggested_vibe": "Moody solarpunk-meets-cyberpunk, bioluminescent light accents, amber and green highlights",
                "suggested_music_genre": "Contemplative ambient electronic soundtrack, transitioning into a crescendo"
            }
        }

    def _clone_github_repo(self, url: str) -> str:
        """
        Clones a GitHub repository URL into a temporary directory and returns the path.
        Raises RuntimeError if git is unavailable or the clone fails.
        """
        try:
            subprocess.run(["git", "--version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        except Exception:
            raise RuntimeError("[RepoInvestigator] git is not installed or not on PATH. Cannot clone GitHub URL.")

        tmp_dir = tempfile.mkdtemp(prefix="cinerepo_clone_")
        try:
            result = subprocess.run(
                ["git", "clone", "--depth", "1", url, tmp_dir],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                timeout=120,
            )
            if result.returncode != 0:
                shutil.rmtree(tmp_dir, ignore_errors=True)
                raise RuntimeError(
                    f"[RepoInvestigator] git clone failed for '{url}': "
                    f"{result.stderr.decode('utf-8', errors='ignore').strip()}"
                )
        except subprocess.TimeoutExpired:
            shutil.rmtree(tmp_dir, ignore_errors=True)
            raise RuntimeError(f"[RepoInvestigator] git clone timed out for '{url}'.")
        return tmp_dir

    def analyze(
        self,
        repo_path: str,
        mock_mode: bool = False,
    ) -> dict:
        """
        Analyzes a repository directory or GitHub URL, reading key codebase structures and READMEs.
        If a GitHub URL is provided it is cloned to a temp directory first.
        If mock_mode is True or GEMINI_API_KEY is missing, returns cached Hermes Agent analysis.
        Ambient suggestions remain open-ended inspiration for the PromptArchitect rather than a prescribed genre or visual treatment.
        Raises RuntimeError on analysis failure so callers can surface it to the user.
        """
        if mock_mode or self.client is None:
            return self._get_mock_data()

        client = self.client

        # Auto-clone GitHub / remote URLs to a local temp dir
        tmp_clone_dir = None
        if repo_path.startswith("http://") or repo_path.startswith("https://"):
            tmp_clone_dir = self._clone_github_repo(repo_path)
            repo_path = tmp_clone_dir

        # Validate path early
        if not os.path.exists(repo_path):
            raise RuntimeError(f"[RepoInvestigator] Path does not exist: '{repo_path}'")

        try:
            file_summaries = []
            max_files = 30
            chars_per_file = 4000
            count = 0

            skip_dirs = {".git", "node_modules", "__pycache__", "dist", "build",
                         ".venv", "venv", "env", ".mypy_cache", ".pytest_cache"}
            code_extensions = {'.py', '.js', '.ts', '.jsx', '.tsx', '.md', '.json',
                                '.txt', '.yaml', '.yml', '.toml', '.go', '.java',
                                '.rs', '.cpp', '.c', '.h', '.rb', '.php', '.cs'}

            # Priority pass: always read README first for high-level context
            for readme_name in ["README.md", "README.rst", "README.txt", "readme.md"]:
                readme_path = os.path.join(repo_path, readme_name)
                if os.path.exists(readme_path):
                    try:
                        with open(readme_path, 'r', encoding='utf-8', errors='ignore') as f:
                            content = f.read(6000)
                            file_summaries.append(f"File: {readme_name} [README - HIGH PRIORITY]\nContent Sample:\n{content}\n")
                            count += 1
                    except Exception:
                        pass
                    break

            # Walk remaining files
            for root, dirs, files in os.walk(repo_path):
                dirs[:] = [d for d in dirs if d not in skip_dirs and not d.startswith('.')]

                for file in files:
                    if count >= max_files:
                        break
                    ext = os.path.splitext(file)[1].lower()
                    if ext not in code_extensions:
                        continue
                    if file.lower() in {"readme.md", "readme.rst", "readme.txt"}:
                        continue
                    file_path = os.path.join(root, file)
                    try:
                        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                            content = f.read(chars_per_file)
                            rel_path = os.path.relpath(file_path, repo_path)
                            file_summaries.append(f"File: {rel_path}\nContent Sample:\n{content}\n")
                            count += 1
                    except Exception:
                        pass

                if count >= max_files:
                    break

            if not file_summaries:
                raise RuntimeError(
                    f"[RepoInvestigator] No readable source files found in '{repo_path}'. "
                    "Check that the path is correct and contains code files."
                )

            codebase_context = "\n---\n".join(file_summaries)
            ambient_direction = (
                "- Offer an optional metaphor, visual approach, and music approach that fit the repository. "
                "- They may use any genre, medium, or emotional structure; DO NOT ASSUME science fiction, fantasy, photorealism, or a fixed color palette.\n"
                "- Treat ambient as inspiration for the next agent, not a binding art direction."
            )
            prompt = f"""
            You are a Senior Software Architect and a Creative Art Director working together.
            Analyze this codebase and translate its architecture into a highly visual, metaphorical story for a short video showcase.

            Step 1: Understand the tech. Name the project, its core purpose, critical modules, and languages used.
            Step 2: Choose an Ambient Music and Art Direction profile (ambient):
            {ambient_direction}

            Codebase context:
            {codebase_context}

            Return ONLY a valid JSON object. No markdown, no comments, no trailing commas.
            """

            response = client.models.generate_content(
                model='gemini-3.5-flash',
                contents=prompt,
                config=types.GenerateContentConfig(
                    response_mime_type="application/json",
                    response_schema=RepoAnalysisSchema,   # ← Schema lock: forces valid JSON
                ),
            )

            # Prefer the SDK's parsed object when available (response_schema path)
            if hasattr(response, 'parsed') and response.parsed is not None:
                parsed = cast(RepoAnalysisSchema, response.parsed)
                return {
                    "repo_name": parsed.repo_name,
                    "core_purpose": parsed.core_purpose,
                    "architecture_components": [
                        {"name": c.name, "purpose": c.purpose}
                        for c in parsed.architecture_components
                    ],
                    "technologies_used": parsed.technologies_used,
                    "ambient": {
                        "metaphor_theme": parsed.ambient.metaphor_theme,
                        "suggested_vibe": parsed.ambient.suggested_vibe,
                        "suggested_music_genre": parsed.ambient.suggested_music_genre,
                    }
                }

            # Fallback: robust multi-stage text parser
            if response.text is None:
                raise RuntimeError("[RepoInvestigator] GenAI responded with empty text.")
            return robust_parse_json(response.text)

        except RuntimeError:
            raise  # Re-raise validation/path errors as-is
        except Exception as e:
            raise RuntimeError(f"[RepoInvestigator] Gemini analysis failed: {e}")
        finally:
            if tmp_clone_dir:
                shutil.rmtree(tmp_clone_dir, ignore_errors=True)
