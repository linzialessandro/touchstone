# Get value by JSON-like pointer

Implement:

```python
def pointer_get(doc: object, pointer: str) -> object:
    ...
```

## Spec

- `pointer` is `""` (whole doc) or starts with `/` and uses `/`-separated tokens.
- Tokens name dict keys or decimal list indices (`"0"`, `"1"`, ...).
- No `~` escaping required (inputs won't contain escaped tokens).
- If any step is missing / wrong type / bad index, raise `KeyError`.
- Dict keys are strings; list indices must be canonical non-negative integers without leading zeros (except `"0"`).

## Examples

`doc={"a":[{"b":2}]}`, pointer `"/a/0/b"` → `2`  
`pointer=""` → entire `doc`
