# Prefix autocomplete

Implement:

```python
def autocomplete(words: list[str], prefix: str, k: int) -> list[str]:
    ...
```

## Spec

- Return up to `k` words from `words` that start with `prefix`.
- Results sorted lexicographically ascending.
- If more than `k` matches, keep the first `k` after sorting.
- `k >= 0`; `k == 0` → `[]`.
- Case-sensitive. Duplicate words in input: treat multiset (duplicates may appear multiple times if present).

## Example

`words=["apple","app","application","banana"]`, `prefix="app"`, `k=2` → `["app","apple"]`
