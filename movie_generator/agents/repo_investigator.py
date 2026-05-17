import os
import json
from typing import List
from pydantic import BaseModel
from google import genai
from google.genai import types
from movie_generator.agents.json_utils import robust_parse_json


# ── Output schema — forces Gemini to produce well-formed JSON ─────────────────
class ArchitectureComponent(BaseModel):
    name: str
    purpose: str

class RepoAnalysisSchema(BaseModel):
    repo_name: str
    core_purpose: str
    architecture_components: List[ArchitectureComponent]
    technologies_used: List[str]


class RepoInvestigator:
    def __init__(self, client: genai.Client = None):
        self.client = client or (genai.Client() if os.environ.get("GEMINI_API_KEY") else None)

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
            "technologies_used": ["Python", "SQLite", "FTS5", "RPC", "Markdown Skills"]
        }

    def analyze(self, repo_path: str, mock_mode: bool = False) -> dict:
        """
        Analyzes a repository directory, reading key codebase structures and READMEs.
        If mock_mode is True or GEMINI_API_KEY is missing, returns cached Hermes Agent analysis.
        Raises RuntimeError on analysis failure so callers can surface it to the user.
        """
        if mock_mode or not self.client:
            return self._get_mock_data()

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
            prompt = f"""
            You are a senior software architect analyzing a codebase.
            Based on the files below, extract:
            1. The name of the project.
            2. The core purpose of the project in one clear sentence.
            3. The 3-4 most critical architecture components, databases, patterns, or tools and what they do.
            4. The primary programming languages and technologies used.

            Codebase context:
            {codebase_context}

            Return ONLY a valid JSON object. No markdown, no comments, no trailing commas.
            """

            response = self.client.models.generate_content(
                model='gemini-2.5-flash',
                contents=prompt,
                config=types.GenerateContentConfig(
                    response_mime_type="application/json",
                    response_schema=RepoAnalysisSchema,   # ← Schema lock: forces valid JSON
                ),
            )

            # Prefer the SDK's parsed object when available (response_schema path)
            if hasattr(response, 'parsed') and response.parsed is not None:
                parsed = response.parsed
                return {
                    "repo_name": parsed.repo_name,
                    "core_purpose": parsed.core_purpose,
                    "architecture_components": [
                        {"name": c.name, "purpose": c.purpose}
                        for c in parsed.architecture_components
                    ],
                    "technologies_used": parsed.technologies_used
                }

            # Fallback: robust multi-stage text parser
            return robust_parse_json(response.text)

        except RuntimeError:
            raise  # Re-raise validation/path errors as-is
        except Exception as e:
            raise RuntimeError(f"[RepoInvestigator] Gemini analysis failed: {e}")
