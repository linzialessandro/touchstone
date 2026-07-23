def ring_sum(matrix: list[list[int]], k: int) -> int:
    if not matrix or not matrix[0] or k < 0:
        return 0
    m, n = len(matrix), len(matrix[0])
    if k * 2 >= m or k * 2 >= n:
        return 0
    total = 0
    top, bottom = k, m - 1 - k
    left, right = k, n - 1 - k
    for j in range(left, right + 1):
        total += matrix[top][j]
    for i in range(top + 1, bottom + 1):
        total += matrix[i][right]
    if bottom > top:
        for j in range(right - 1, left - 1, -1):
            total += matrix[bottom][j]
    if right > left:
        for i in range(bottom - 1, top, -1):
            total += matrix[i][left]
    return total
