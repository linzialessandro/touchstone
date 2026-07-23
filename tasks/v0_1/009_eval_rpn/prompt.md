# Evaluate reverse Polish notation

Implement:

```python
def eval_rpn(tokens: list[str]) -> int:
    ...
```

## Spec

- Tokens are integers (as strings, possibly negative) or operators `+`, `-`, `*`, `/`.
- `/` is **truncated toward zero** (like C/Java), not floor division.
- Evaluation uses a stack; operators pop two operands `b` then `a` meaning `a OP b`.
- Assume the expression is valid and fits in 32-bit signed range for intermediate results is not required—use Python ints.
- Empty token list → raise `ValueError`.

## Example

`["2","1","+","3","*"]` → `9`
