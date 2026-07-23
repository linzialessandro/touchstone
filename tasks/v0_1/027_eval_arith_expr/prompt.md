# Evaluate arithmetic expression string

Implement:

```python
def eval_expr(expr: str) -> int:
    ...
```

## Spec

- `expr` contains non-negative integers, `+`, `-`, `*`, `/`, spaces, and parentheses `()`.
- `/` is **truncated toward zero**.
- Standard precedence: `*` `/` over `+` `-`; parentheses override.
- Unary minus is **not** required (no leading `-` on numbers except as binary operator).
- Empty / invalid → raise `ValueError`.

## Example

`"3+2*2"` → `7`; `"(1+(4+5+2)-3)+(6+8)"` → `23`
