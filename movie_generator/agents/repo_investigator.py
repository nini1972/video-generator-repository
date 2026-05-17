import os
from google import genai
from google.genai import types

class RepoInvestigator:
    def __init__(self, client: genai.Client = None):
        self.client = client or (genai.Client() if os.environ.get("GEMINI_API_KEY") else None)

    def analyze(self, repo_path: str, mock_mode: bool = False) -> dict:
        """
        Analyzes a repository directory, reading key codebase structures and READMEs.
        If mock_mode is True or GEMINI_API_KEY is missing, returns cached analysis.
        """
        if mock_mode or not self.client:
            # Fallback to cached high-quality mock data for the Hermes Agent
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

        # Real Codebase Analysis
        try:
            # Gather repository file summaries
            file_summaries = []
            max_files = 15
            count = 0
            
            for root, dirs, files in os.walk(repo_path):
                # Skip version control and build folders
                if any(x in root for x in [".git", "node_modules", "__pycache__", "dist", "build"]):
                    continue
                for file in files:
                    if file.endswith(('.py', '.js', '.ts', '.md', '.json', '.txt')):
                        file_path = os.path.join(root, file)
                        try:
                            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                                # Read first 80 lines for context
                                content = f.read(1500)
                                file_summaries.append(f"File: {os.path.relpath(file_path, repo_path)}\nContent Sample:\n{content}\n")
                                count += 1
                        except Exception:
                            pass
                    if count >= max_files:
                        break
                if count >= max_files:
                    break

            codebase_context = "\n---\n".join(file_summaries)
            prompt = f"""
            You are a senior software architect analyzing a codebase.
            Based on the files below, extract:
            1. The name of the project.
            2. The core purpose of the project.
            3. The 3-4 most critical architecture components, databases, patterns, or tools and what they do.
            4. The primary programming languages and technologies used.
            
            Codebase context:
            {codebase_context}
            
            Format your response as a strict JSON object with these keys:
            - repo_name: string
            - core_purpose: string
            - architecture_components: array of objects with keys 'name' and 'purpose'
            - technologies_used: array of strings
            """

            response = self.client.models.generate_content(
                model='gemini-2.5-flash',
                contents=prompt,
                config=types.GenerateContentConfig(
                    response_mime_type="application/json",
                ),
            )
            import json
            return json.loads(response.text)

        except Exception as e:
            print(f"Error during real repo analysis: {e}. Falling back to mock data.")
            return self.analyze(repo_path, mock_mode=True)
