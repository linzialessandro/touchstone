# Stable partition by predicate

Implement:

```python
def stable_partition(items: list[int], pivot: int) -> list[int]:
    ...
```

## Spec

Return a new list: all elements `< pivot` first, then all elements `>= pivot`.
Within each part, preserve original relative order (stable).
Do not mutate the input list.

## Example

`[5,1,4,2,3], pivot=3` → `[1,2,5,4,3]`
