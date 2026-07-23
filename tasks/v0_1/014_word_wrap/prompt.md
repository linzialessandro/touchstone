# Greedy word wrap

Implement:

```python
def word_wrap(text: str, width: int) -> list[str]:
    ...
```

## Spec

1. Split `text` on whitespace into words (no empty words).
2. If any word is longer than `width`, raise `ValueError`.
3. Pack words greedily into lines without exceeding `width`.
4. Words on a line separated by a single space.
5. `width >= 1`. Empty text → `[]`.

## Example

`word_wrap("hello world ok", 5)` → `["hello", "world", "ok"]`
