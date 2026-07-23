# K-th element of two sorted arrays

Implement:

```python
def kth_sorted(a: list[int], b: list[int], k: int) -> int:
    ...
```

## Spec

- `a` and `b` are individually sorted ascending (may be empty).
- `k` is **1-based** index in the merged multiset (`k=1` is the smallest).
- Return the k-th smallest in the merged sequence without fully merging if possible.
- If `k` is out of range `1 .. len(a)+len(b)`, raise `IndexError`.

## Example

`a=[1,3,5]`, `b=[2,4,6]`, `k=4` → `4`
