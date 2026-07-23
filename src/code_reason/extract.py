"""Extract code from model responses."""

from __future__ import annotations

import re

FENCE_RE = re.compile(r"```(?:python|py)?\s*\n(.*?)```", re.DOTALL | re.IGNORECASE)


def extract_python_code(text: str) -> str:
    """Prefer fenced python blocks; otherwise return stripped full text."""
    matches = FENCE_RE.findall(text)
    if matches:
        # If multiple fences, join with blank lines (common: solution + helpers).
        return "\n\n".join(m.strip() for m in matches if m.strip())
    return text.strip()
