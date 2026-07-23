# Fix a racy counter

Implement a thread-safe counter:

```python
class Counter:
    def __init__(self) -> None:
        ...

    def increment(self) -> None:
        """Atomically add 1 to the counter."""
        ...

    @property
    def value(self) -> int:
        """Current value (consistent read)."""
        ...
```

## Requirements

- Start at `0`.
- Many threads will call `increment()` concurrently.
- After all threads join, `value` must equal the total number of successful increments.
- Use the standard library only (`threading` is fine).
- Do not sleep to “make races less likely”; fix the actual race.

## Hint (allowed)

A bare `self._value += 1` without synchronization is not enough under concurrency.
