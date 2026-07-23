# Topological sort of modules

Implement:

```python
def topo_sort(n: int, edges: list[tuple[int, int]]) -> list[int]:
    ...
```

## Spec

- Nodes are integers `0 .. n-1`.
- Each edge `(u, v)` means **u must come before v** (u → v dependency direction: u first).
- Return one valid topological order as a list of all `n` nodes.
- If a cycle exists (or not all nodes orderable), return `[]`.
- Among valid orders, any is acceptable (tests accept any valid order or empty).

## Example

`n=4`, edges `[(0,1),(0,2),(1,3),(2,3)]` → e.g. `[0,1,2,3]` or `[0,2,1,3]`
