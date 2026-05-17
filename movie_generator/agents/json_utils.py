"""
Shared JSON parsing utilities for the CineRepo agent pipeline.

Gemini's JSON output can contain several non-standard patterns:
  - Markdown code fences (```json ... ```)
  - Trailing commas before } or ]  (valid JS, illegal JSON)
  - Single-line // comments
  - Multi-line /* */ comments
  - Bare JSON embedded inside prose text

This module applies progressive cleaning stages so any of those
formats are handled gracefully before falling back to an error.
"""

import re
import json


def robust_parse_json(text: str) -> dict:
    """
    Multi-stage JSON parser that handles common Gemini output quirks.

    Stages (applied in order until one succeeds):
      1. Direct parse (fast path — valid JSON as-is)
      2. Strip markdown code fences, re-parse
      3. Remove trailing commas, re-parse
      4. Strip JS-style comments, re-parse
      5. Extract the largest {...} block from surrounding prose, re-parse
      6. Apply all cleanings to extracted block, re-parse (last resort)

    Raises json.JSONDecodeError if all stages fail.
    """
    original = text.strip()

    # ── Stage 1: fast path ────────────────────────────────────────────────────
    try:
        return json.loads(original)
    except json.JSONDecodeError:
        pass

    # ── Stage 2: strip markdown fences ───────────────────────────────────────
    fenced = _strip_fences(original)
    try:
        return json.loads(fenced)
    except json.JSONDecodeError:
        pass

    # ── Stage 3: remove trailing commas ──────────────────────────────────────
    no_trailing = _remove_trailing_commas(fenced)
    try:
        return json.loads(no_trailing)
    except json.JSONDecodeError:
        pass

    # ── Stage 4: strip JS comments ────────────────────────────────────────────
    no_comments = _strip_js_comments(no_trailing)
    try:
        return json.loads(no_comments)
    except json.JSONDecodeError:
        pass

    # ── Stage 5: extract outermost { } block from prose ───────────────────────
    extracted = _extract_json_block(original)
    if extracted and extracted != original:
        try:
            return json.loads(extracted)
        except json.JSONDecodeError:
            pass

        # ── Stage 6: all cleanings on extracted block ─────────────────────────
        cleaned = _strip_js_comments(_remove_trailing_commas(extracted))
        try:
            return json.loads(cleaned)
        except json.JSONDecodeError:
            pass

    # Nothing worked — surface the original error
    raise json.JSONDecodeError(
        f"robust_parse_json: all parsing stages failed.\n"
        f"First 300 chars of response:\n{original[:300]}",
        original, 0
    )


# ── Private helpers ───────────────────────────────────────────────────────────

def _strip_fences(text: str) -> str:
    """Remove ```json ... ``` or ``` ... ``` wrappers."""
    match = re.search(r'```(?:json)?\s*([\s\S]+?)```', text)
    return match.group(1).strip() if match else text


def _remove_trailing_commas(text: str) -> str:
    """Remove trailing commas before ] or } (e.g. [1, 2,] -> [1, 2])."""
    # Handle commas followed by optional whitespace then ] or }
    return re.sub(r',(\s*[}\]])', r'\1', text)


def _strip_js_comments(text: str) -> str:
    """Remove // single-line and /* */ multi-line comments from JSON-like text."""
    # Multi-line comments first
    text = re.sub(r'/\*[\s\S]*?\*/', '', text)
    # Single-line comments (careful not to strip URLs like https://)
    text = re.sub(r'(?<![:/])//[^\n]*', '', text)
    return text


def _extract_json_block(text: str) -> str:
    """
    Find the outermost { ... } block in a string of mixed prose + JSON.
    Returns the block, or the original text if no block found.
    """
    start = text.find('{')
    if start == -1:
        return text
    # Walk forward matching braces
    depth = 0
    in_string = False
    escape = False
    for i, ch in enumerate(text[start:], start):
        if escape:
            escape = False
            continue
        if ch == '\\' and in_string:
            escape = True
            continue
        if ch == '"' and not escape:
            in_string = not in_string
            continue
        if in_string:
            continue
        if ch == '{':
            depth += 1
        elif ch == '}':
            depth -= 1
            if depth == 0:
                return text[start:i + 1]
    return text
