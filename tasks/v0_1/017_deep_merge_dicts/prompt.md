# Deep merge dictionaries

Implement:

```python
def deep_merge(a: dict, b: dict) -> dict:
    ...
```

## Spec

Return a **new** dict (do not mutate inputs):

1. Keys only in `a` or only in `b`: take that value (shallow copy of top-level reference is fine for non-dict values).
2. If both values are `dict`, merge recursively.
3. If both values are `list`, concatenate `a_list + b_list`.
4. Otherwise `b` wins (overwrite).
5. Nested results follow the same rules.

## Example

`{"x":1,"d":{"y":2},"k":[1]}` merge `{"x":9,"d":{"z":3},"k":[2]}` →
`{"x":9,"d":{"y":2,"z":3},"k":[1,2]}`
