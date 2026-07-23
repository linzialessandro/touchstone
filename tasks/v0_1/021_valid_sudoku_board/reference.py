def is_valid_sudoku(board: list[list[str]]) -> bool:
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    blocks = [set() for _ in range(9)]
    for i in range(9):
        for j in range(9):
            v = board[i][j]
            if v == ".":
                continue
            b = (i // 3) * 3 + (j // 3)
            if v in rows[i] or v in cols[j] or v in blocks[b]:
                return False
            rows[i].add(v)
            cols[j].add(v)
            blocks[b].add(v)
    return True
