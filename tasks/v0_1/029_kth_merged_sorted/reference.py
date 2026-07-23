def kth_sorted(a: list[int], b: list[int], k: int) -> int:
    n, m = len(a), len(b)
    if k < 1 or k > n + m:
        raise IndexError("k")
    # ensure a is smaller
    if n > m:
        return kth_sorted(b, a, k)
    if n == 0:
        return b[k - 1]
    if k == 1:
        return min(a[0], b[0])
    i = min(n, k // 2)
    j = k - i
    if a[i - 1] <= b[j - 1]:
        return kth_sorted(a[i:], b, k - i)
    return kth_sorted(a, b[j:], k - j)
