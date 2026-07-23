# Sliding window maximum

Implement a function:

```python
def max_sliding_window(nums: list[int], k: int) -> list[int]:
    ...
```

## Specification

- `nums` is a list of integers (may be empty).
- `k` is the window size.
- If `k <= 0` or `nums` is empty, return `[]`.
- If `k > len(nums)`, treat the whole array as one window when `k` is positive… **No:** if `k > len(nums)` and `nums` is non-empty, return `[]` (invalid window).
- Otherwise, return a list `out` of length `len(nums) - k + 1` where `out[i]` is the maximum of `nums[i : i+k]`.

## Constraints for your solution

- Target better than naive O(n·k) if n is large; O(n) time with a deque (or equivalent) is expected for full credit in spirit, but **grading is by tests only**.
- Do not read from stdin or write to stdout.
- Put the function in the top-level module (the grader imports/`exec`s your file as `solution.py` and runs tests against it).

## Example

Input: `nums = [1, 3, -1, -3, 5, 3, 6, 7]`, `k = 3`  
Output: `[3, 3, 5, 5, 6, 7]`
