# Free time slots in a day

Implement:

```python
def free_slots(busy: list[tuple[int, int]], day_start: int, day_end: int) -> list[tuple[int, int]]:
    ...
```

## Spec

- Time is an integer timeline; half-open intervals `[start, end)`.
- `busy` entries may overlap and be unsorted; ignore empty/invalid where `start >= end`.
- Clip busy intervals to `[day_start, day_end)`.
- Return maximal free half-open slots inside the day, sorted.
- If `day_start >= day_end`, return `[]`.

## Example

day `[0, 10)`, busy `[(1,3),(2,4),(7,8)]` → `[(0,1),(4,7),(8,10)]`
