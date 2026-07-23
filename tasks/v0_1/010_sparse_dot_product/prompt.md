# Sparse vector dot product

Implement:

```python
def sparse_dot(a: dict[int, float], b: dict[int, float]) -> float:
    ...
```

## Spec

- Vectors are maps index → value; missing index means `0`.
- Return sum over indices of `a[i] * b[i]` for indices present in **both**.
- Ignore zero-valued entries if present (treat as zero contribution).
- Empty dicts allowed; result `0.0`.

## Example

`{0:1.0, 2:3.0}` · `{2:4.0, 5:1.0}` → `12.0`
