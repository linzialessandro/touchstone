"""Touchstone: stable_partition — executable grading via script_runner.

Designed with Grok (designer only). Open models compete.
"""

from __future__ import annotations

import kaggle_benchmarks as kbench

PROMPT = """You are solving a coding evaluation task for the Touchstone benchmark.

Return a complete Python solution in a single markdown fence (```python ... ```).
Include the full function. Explanations outside the fence are optional.

# Stable partition by predicate

Implement:

```python
def stable_partition(items: list[int], pivot: int) -> list[int]:
    ...
```

## Spec

Return a new list: all elements `< pivot` first, then all elements `>= pivot`.
Within each part, preserve original relative order (stable).
Do not mutate the input list.

## Example

`[5,1,4,2,3], pivot=3` → `[1,2,5,4,3]`
"""


@kbench.task(
    name="touchstone-stable-partition",
    description=(
        "Touchstone: implement stable_partition(items, pivot). "
        "Graded by executable checks. Designed with Grok; open models compete."
    ),
)
def touchstone_stable_partition(llm) -> bool:
    try:
        response = llm.prompt(PROMPT)
    except Exception:
        return False

    text = response if isinstance(response, str) else str(response)
    try:
        code = kbench.tools.python.extract_code(text)
    except Exception:
        code = text

    if not code or "stable_partition" not in str(code):
        return False

    harness = (
        str(code).strip()
        + """

# --- Touchstone executable checks ---
_src = [5, 1, 4, 2, 3]
_out = stable_partition(_src, 3)
assert _out == [1, 2, 5, 4, 3], _out
assert _src == [5, 1, 4, 2, 3], "must not mutate input"
assert stable_partition([], 0) == []
assert stable_partition([1, 2, 3], 0) == [1, 2, 3]
assert stable_partition([1, 2, 3], 9) == [1, 2, 3]
print("OK")
"""
    )
    try:
        result = kbench.tools.python.script_runner.run_code(harness)
    except Exception:
        return False

    ok = getattr(result, "exit_code", 1) == 0 and "OK" in (getattr(result, "stdout", "") or "")
    return bool(ok)


touchstone_stable_partition.run(kbench.llm)
