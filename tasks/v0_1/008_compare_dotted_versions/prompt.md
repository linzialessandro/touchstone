# Compare dotted version strings

Implement:

```python
def cmp_version(a: str, b: str) -> int:
    ...
```

## Spec

- Versions are non-empty strings of non-negative integers separated by `.` (e.g. `"1.0.3"`).
- Missing segments are treated as `0` (so `"1.0"` equals `"1.0.0"`).
- Compare segment-wise as integers from the left.
- Return `-1` if `a < b`, `0` if equal, `1` if `a > b`.
- Empty segment (e.g. `"1..2"`) is invalid → raise `ValueError`.
- Non-digit segments → raise `ValueError`.

## Examples

- `cmp_version("1.2", "1.2.0")` → `0`
- `cmp_version("1.10", "1.2")` → `1`
- `cmp_version("0.1", "1.0")` → `-1`
