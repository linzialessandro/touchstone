# Token bucket rate limiter

Implement:

```python
class TokenBucket:
    def __init__(self, capacity: int, refill_rate: float) -> None:
        """capacity tokens max; refill_rate tokens per second."""
        ...

    def allow(self, timestamp: float, tokens: int = 1) -> bool:
        """Return True if `tokens` can be consumed at `timestamp` (seconds, non-decreasing calls)."""
        ...
```

## Spec

- Start full at the first `allow` time (or t=0 with full capacity — tests use non-decreasing timestamps).
- Between calls, refill `refill_rate * dt` tokens, capped at `capacity`.
- If enough tokens, consume and return True; else return False without consuming.
- `capacity >= 1`, `refill_rate >= 0`, `tokens >= 1`.
- Floating timestamps; use continuous refill.

## Example

capacity 2, rate 1.0: allow(0) True, allow(0) True, allow(0) False, allow(1.0) True
