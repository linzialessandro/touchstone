# Balanced delimiter score

Implement:

```python
def balanced_score(s: str) -> int:
    ...
```

## Spec

Only characters `(`, `)`, `[`, `]` matter; **ignore all other characters**.

Scan left to right with a stack of opening brackets.

- Encounter `(` or `[`: push it. Score does not change.
- Encounter `)`: if top is `(`, pop and add **1** to score. Else return **-1** (invalid).
- Encounter `]`: if top is `[`, pop and add **2** to score. Else return **-1**.
- If at any close the stack is empty → **-1**.
- After full scan, if stack non-empty → **-1**.
- Empty string (or only ignored chars) → **0**.

## Examples

- `"()"` → `1`
- `"[]"` → `2`
- `"([)]"` → `-1`
- `"a(b)c[d]"` → `1+2 = 3`
- `"(()"` → `-1`
