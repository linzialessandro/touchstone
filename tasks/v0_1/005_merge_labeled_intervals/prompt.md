# Merge labeled intervals

Implement:

```python
def merge_labeled(intervals: list[tuple[int, int, str]]) -> list[tuple[int, int, str]]:
    ...
```

Each interval is `(start, end, label)` with `start <= end` (inclusive endpoints for overlap checks).

## Spec

1. Ignore intervals where `start > end` (drop them).
2. Sort remaining by `start` ascending, then `end` ascending.
3. Merge **overlapping or touching** intervals only if they share the **same label**.
   - Touching: `a.end + 1 >= b.start` (integer line).
4. Different labels never merge, even if overlapping.
5. When merging same label, new interval is `(min starts, max ends, label)`.
6. Return merged list sorted by start, then end, then label.

## Example

`[(1,3,"a"), (2,5,"a"), (4,6,"b")]` → `[(1,5,"a"), (4,6,"b")]`
