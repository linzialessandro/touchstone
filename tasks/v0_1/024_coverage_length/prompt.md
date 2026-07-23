# Covered length of union of intervals

Implement:

```python
def coverage_length(intervals: list[tuple[int, int]]) -> int:
    ...
```

## Spec

- Half-open intervals `[start, end)` on integers.
- Drop invalid `start >= end`.
- Return the total number of integer points covered by the union
  (equivalently, total measure of the union).
- Example: `[1,4) U [3,6) U [8,9)` covers length `5 + 1 = 6`.

## Example

`[(1,4),(3,6),(8,9)]` → `6`
