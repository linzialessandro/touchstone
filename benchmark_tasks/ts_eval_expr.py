# Touchstone hard task: arithmetic expression evaluation (executable grading).
import kaggle_benchmarks as kbench

PROMPT = """You are solving a HARD coding task for the Touchstone benchmark.
Return a complete Python solution in one markdown fence (```python ... ```).
Include the full function. No omitted code.

# Evaluate arithmetic expression string

Implement:

```python
def eval_expr(expr: str) -> int:
    ...
```

## Spec

- `expr` contains non-negative integers, `+`, `-`, `*`, `/`, spaces, and parentheses `()`.
- `/` is **truncated toward zero** (like C/Java int division of signs, not floor div for negatives in tests we use non-negative results).
- Standard precedence: `*` and `/` over `+` and `-`; parentheses override.
- Unary minus is NOT required.
- Empty or invalid expression -> raise ValueError.

## Examples

- eval_expr("3+2*2") -> 7
- eval_expr("(1+(4+5+2)-3)+(6+8)") -> 23
- eval_expr(" 3+5 / 2 ") -> 5
- eval_expr("14-3*2") -> 8
- eval_expr("2*(3+4)") -> 14
"""


@kbench.task(
    name="ts-eval-expr",
    description="Touchstone HARD: eval_expr with precedence and parens; executable asserts.",
)
def ts_eval_expr(llm) -> bool:
    try:
        response = llm.prompt(PROMPT)
    except Exception:
        return False
    try:
        code = kbench.tools.python.extract_code(response)
    except Exception:
        return False
    if not code or "eval_expr" not in code:
        return False
    prog = (
        code
        + """
assert eval_expr("3+2*2") == 7
assert eval_expr("(1+(4+5+2)-3)+(6+8)") == 23
assert eval_expr(" 3+5 / 2 ") == 5
assert eval_expr("14-3*2") == 8
assert eval_expr("2*(3+4)") == 14
try:
    eval_expr("")
    raise AssertionError("empty should raise")
except ValueError:
    pass
print("OK")
"""
    )
    try:
        out = kbench.tools.python.script_runner.run_code(prog)
    except Exception:
        return False
    return out.exit_code == 0 and "OK" in (out.stdout or "")


ts_eval_expr.run(kbench.llm)
