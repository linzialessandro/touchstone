# Circular circuit start index

Implement:

```python
def circuit_start(gas: list[int], cost: list[int]) -> int:
    ...
```

## Spec

- `gas[i]` fuel gained at station `i`; `cost[i]` fuel to go from `i` to `i+1` (mod n).
- Find the **unique** starting index that allows a full circuit without tank going negative (start tank 0).
- If impossible, return `-1`.
- If multiple starts would work, return the **smallest** index (for these tests uniqueness holds when possible).
- `len(gas) == len(cost) >= 1`.

## Example

`gas=[1,2,3,4,5]`, `cost=[3,4,5,1,2]` → `3`
