"""Deterministic mock provider for offline dry-runs and unit tests.

Golden mode loads each task's reference.py so the mock scales with the suite.
"""

from __future__ import annotations

import json
import time
from pathlib import Path

from code_reason.loader import DEFAULT_TASKS_DIR
from code_reason.providers.base import CompletionResult, Provider


class MockProvider(Provider):
    name = "mock"

    def __init__(self, mode: str = "golden", tasks_dir: Path | None = None) -> None:
        """mode: golden | empty | garbage"""
        self.mode = mode
        self.tasks_dir = tasks_dir or DEFAULT_TASKS_DIR

    def complete(self, prompt: str, *, model: str, system: str | None = None) -> CompletionResult:
        t0 = time.perf_counter()
        task_id = _detect_task_id(prompt)
        if self.mode == "empty":
            text = "I don't know."
        elif self.mode == "garbage":
            text = "```python\nprint('hello')\n```"
        else:
            code = _load_reference(self.tasks_dir, task_id)
            if code is None:
                code = (
                    "def solution():\n"
                    "    raise NotImplementedError('no reference.py for mock')\n"
                )
            text = f"Here is a solution:\n\n```python\n{code}\n```"
        ms = (time.perf_counter() - t0) * 1000
        return CompletionResult(text=text, latency_ms=ms, raw={"mode": self.mode, "task_id": task_id})


def _detect_task_id(prompt: str) -> str | None:
    for line in prompt.splitlines():
        if line.startswith("TASK_ID:"):
            return line.split(":", 1)[1].strip()
    return None


def _load_reference(tasks_dir: Path, task_id: str | None) -> str | None:
    if not task_id or not tasks_dir.exists():
        return None
    direct = tasks_dir / task_id / "reference.py"
    if direct.exists():
        return direct.read_text(encoding="utf-8")
    for child in tasks_dir.iterdir():
        if not child.is_dir():
            continue
        meta = child / "task.json"
        ref = child / "reference.py"
        if not meta.exists() or not ref.exists():
            continue
        try:
            data = json.loads(meta.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        if data.get("id") == task_id:
            return ref.read_text(encoding="utf-8")
    return None
