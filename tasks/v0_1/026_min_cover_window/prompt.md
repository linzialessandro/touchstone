# Minimum covering window

Implement:

```python
def min_cover_window(s: str, need: dict[str, int]) -> str:
    ...
```

## Spec

Return the **shortest** substring of `s` that contains at least `need[c]` occurrences of each character `c` in `need`.
If multiple shortest windows exist, return the **leftmost**.
If impossible, return `""`.
Characters not in `need` may appear freely inside the window.
Empty `need` → `""`.
`need` counts are positive integers.

## Example

`s="ADOBECODEBANC"`, `need={"A":1,"B":1,"C":1}` → `"BANC"`
