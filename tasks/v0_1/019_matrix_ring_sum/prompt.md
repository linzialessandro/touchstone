# Sum of matrix ring

Implement:

```python
def ring_sum(matrix: list[list[int]], k: int) -> int:
    ...
```

## Spec

- `matrix` has `m` rows and `n` columns, `m,n >= 1`, rectangular.
- Ring `k=0` is the outer border; `k=1` is one layer inward, etc.
- Sum all elements on ring `k` **without double-counting corners**.
- If ring `k` does not exist, return `0`.
- Single-row or single-column rings still work (the whole remaining line).

## Example

```
1 2 3
4 5 6
7 8 9
```
`k=0` → `1+2+3+6+9+8+7+4 = 40`; `k=1` → `5`
