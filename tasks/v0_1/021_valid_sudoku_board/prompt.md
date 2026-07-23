# Validate partial Sudoku board

Implement:

```python
def is_valid_sudoku(board: list[list[str]]) -> bool:
    ...
```

## Spec

- `board` is 9×9 of strings: digits `'1'`–`'9'` or `'.'` (empty).
- Valid means no digit repeat in any row, column, or 3×3 block.
- Empty cells are fine; do **not** solve the puzzle.
- Assume shape is 9×9.

## Example

A correctly filled empty-heavy board with no conflicts → `True`; duplicate in a row → `False`.
