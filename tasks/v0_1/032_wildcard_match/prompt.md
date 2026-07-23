# Wildcard matching

Implement:

```python
def is_match(s: str, p: str) -> bool:
    ...
```

## Spec

- `p` may contain `?` (exactly one char) and `*` (any sequence including empty).
- Other pattern chars match literally.
- Match must cover the **entire** string `s`.

## Example

`is_match("adceb", "*a*b")` → `True`; `is_match("acdcb", "a*c?b")` → `False`
