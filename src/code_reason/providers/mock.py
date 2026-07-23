"""Deterministic mock provider for offline dry-runs and unit tests."""

from __future__ import annotations

import time

from code_reason.providers.base import CompletionResult, Provider

# Minimal correct solutions keyed by task id — only for local plumbing tests.
_GOLDEN: dict[str, str] = {
    "001_sliding_window_max": '''
def max_sliding_window(nums: list[int], k: int) -> list[int]:
    from collections import deque
    if k <= 0 or not nums or k > len(nums):
        return []
    dq: deque[int] = deque()
    out: list[int] = []
    for i, x in enumerate(nums):
        while dq and dq[0] <= i - k:
            dq.popleft()
        while dq and nums[dq[-1]] <= x:
            dq.pop()
        dq.append(i)
        if i >= k - 1:
            out.append(nums[dq[0]])
    return out
'''.strip(),
    "002_parse_ini_sections": '''
def parse_ini_sections(text: str) -> dict[str, dict[str, str]]:
    sections: dict[str, dict[str, str]] = {}
    current: str | None = None
    for raw in text.splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or line.startswith(";"):
            continue
        if line.startswith("[") and line.endswith("]"):
            current = line[1:-1].strip()
            sections.setdefault(current, {})
            continue
        if current is None or "=" not in line:
            continue
        key, _, value = line.partition("=")
        sections[current][key.strip()] = value.strip()
    return sections
'''.strip(),
    "003_race_condition_fix": '''
from threading import Lock

class Counter:
    def __init__(self) -> None:
        self._value = 0
        self._lock = Lock()

    def increment(self) -> None:
        with self._lock:
            self._value += 1

    @property
    def value(self) -> int:
        with self._lock:
            return self._value
'''.strip(),
}


class MockProvider(Provider):
    name = "mock"

    def __init__(self, mode: str = "golden") -> None:
        """mode: golden | empty | garbage"""
        self.mode = mode

    def complete(self, prompt: str, *, model: str, system: str | None = None) -> CompletionResult:
        t0 = time.perf_counter()
        task_id = _detect_task_id(prompt)
        if self.mode == "empty":
            text = "I don't know."
        elif self.mode == "garbage":
            text = "```python\nprint('hello')\n```"
        else:
            code = _GOLDEN.get(task_id, "def solution():\n    raise NotImplementedError\n")
            text = f"Here is a solution:\n\n```python\n{code}\n```"
        ms = (time.perf_counter() - t0) * 1000
        return CompletionResult(text=text, latency_ms=ms, raw={"mode": self.mode, "task_id": task_id})


def _detect_task_id(prompt: str) -> str | None:
    # Prompts include a TASK_ID line for mock routing and debugging.
    for line in prompt.splitlines():
        if line.startswith("TASK_ID:"):
            return line.split(":", 1)[1].strip()
    return None
