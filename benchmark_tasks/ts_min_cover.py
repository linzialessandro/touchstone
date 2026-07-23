# Touchstone hard task: minimum covering window (executable grading).
import kaggle_benchmarks as kbench

PROMPT = """You are solving a HARD coding task for the Touchstone benchmark.
Return a complete Python solution in one markdown fence (```python ... ```).
Include the full function. No omitted code.

# Minimum covering window

Implement:

```python
def min_cover_window(s: str, need: dict[str, int]) -> str:
    ...
```

## Spec

Return the **shortest** substring of `s` that contains at least `need[c]` occurrences of each character `c` in `need`.
If multiple shortest windows exist, return the **leftmost**.
If impossible, return `""`.
Characters not in `need` may appear freely inside the window.
Empty `need` -> `""`.
`need` counts are positive integers.

## Examples

- min_cover_window("ADOBECODEBANC", {"A":1,"B":1,"C":1}) -> "BANC"
- min_cover_window("a", {"a":1}) -> "a"
- min_cover_window("a", {"a":2}) -> ""
- min_cover_window("aa", {"a":2}) -> "aa"
- min_cover_window("xyz", {}) -> ""
"""


@kbench.task(
    name="ts-min-cover",
    description="Touchstone HARD: min_cover_window sliding window; executable asserts.",
)
def ts_min_cover(llm) -> bool:
    try:
        response = llm.prompt(PROMPT)
    except Exception:
        return False
    try:
        code = kbench.tools.python.extract_code(response)
    except Exception:
        return False
    if not code or "min_cover_window" not in code:
        return False
    prog = (
        code
        + """
assert min_cover_window("ADOBECODEBANC", {"A": 1, "B": 1, "C": 1}) == "BANC"
assert min_cover_window("a", {"a": 1}) == "a"
assert min_cover_window("a", {"a": 2}) == ""
assert min_cover_window("aa", {"a": 2}) == "aa"
assert min_cover_window("xyz", {}) == ""
assert min_cover_window("abdecfab", {"a": 1, "b": 1, "c": 1}) == "cfab"
print("OK")
"""
    )
    try:
        out = kbench.tools.python.script_runner.run_code(prog)
    except Exception:
        return False
    return out.exit_code == 0 and "OK" in (out.stdout or "")


ts_min_cover.run(kbench.llm)
