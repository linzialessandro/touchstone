# Touchstone hard task: wildcard matching (executable grading).
import kaggle_benchmarks as kbench

PROMPT = """You are solving a HARD coding task for the Touchstone benchmark.
Return a complete Python solution in one markdown fence (```python ... ```).
Include the full function. No omitted code.

# Wildcard matching

Implement:

```python
def is_match(s: str, p: str) -> bool:
    ...
```

## Spec

- `p` may contain `?` (exactly one char) and `*` (any sequence including empty).
- Other pattern chars match literally.
- Match must cover the **entire** string `s`.

## Examples

- is_match("adceb", "*a*b") -> True
- is_match("acdcb", "a*c?b") -> False
- is_match("", "*") -> True
- is_match("", "?") -> False
- is_match("abc", "a*c") -> True
- is_match("abc", "a?c") -> True
- is_match("abc", "a?b") -> False
"""


@kbench.task(
    name="ts-wildcard",
    description="Touchstone HARD: is_match wildcard DP/search; executable asserts.",
)
def ts_wildcard(llm) -> bool:
    try:
        response = llm.prompt(PROMPT)
    except Exception:
        return False
    try:
        code = kbench.tools.python.extract_code(response)
    except Exception:
        return False
    if not code or "is_match" not in code:
        return False
    prog = (
        code
        + """
assert is_match("adceb", "*a*b") is True
assert is_match("acdcb", "a*c?b") is False
assert is_match("", "*") is True
assert is_match("", "?") is False
assert is_match("abc", "a*c") is True
assert is_match("abc", "a?c") is True
assert is_match("abc", "a?b") is False
print("OK")
"""
    )
    try:
        out = kbench.tools.python.script_runner.run_code(prog)
    except Exception:
        return False
    return out.exit_code == 0 and "OK" in (out.stdout or "")


ts_wildcard.run(kbench.llm)
