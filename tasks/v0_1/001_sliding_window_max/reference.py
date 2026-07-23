"""Reference solution for ownership drills — do not leak into model prompts."""

from collections import deque


def max_sliding_window(nums: list[int], k: int) -> list[int]:
    if k <= 0 or not nums or k > len(nums):
        return []
    dq: deque[int] = deque()
    out: list[int] = []
    for i, x in enumerate(nums):
        while dq and dq[0] <= i - k:
            dq.popleft()
        while dq and nums[dq[-1]] <= x:
            dq.pop()
        dq.append(i)
        if i >= k - 1:
            out.append(nums[dq[0]])
    return out
