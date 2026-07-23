# Minimal LRU cache

Implement class:

```python
class LRUCache:
    def __init__(self, capacity: int) -> None: ...
    def get(self, key: int) -> int: ...
    def put(self, key: int, value: int) -> None: ...
```

## Spec

- `capacity >= 1`.
- `get` returns value or `-1` if missing; a successful get counts as recent use.
- `put` inserts or updates; update counts as recent use.
- When full, `put` of a **new** key evicts the least recently used key.
- Use only the standard library.

## Example

capacity 2: put(1,1), put(2,2), get(1)→1, put(3,3), get(2)→-1
