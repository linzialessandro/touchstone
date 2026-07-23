# Run-length encode letters

Implement:

```python
def rle_encode(s: str) -> str:
    ...
```

## Spec

- Input contains only `A`–`Z` (uppercase) or is empty.
- Encode consecutive runs: letter then decimal count **only if count ≥ 2**; single letters appear alone.
- Example: `"AABCCC"` → `"A2BC3"`
- Empty → `""`.
- If input contains any other character, raise `ValueError`.

## Examples

- `"WWWWB"` → `"W4B"`
- `"ABC"` → `"ABC"`
