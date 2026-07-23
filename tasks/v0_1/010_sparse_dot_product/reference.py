def sparse_dot(a: dict[int, float], b: dict[int, float]) -> float:
    if len(a) > len(b):
        a, b = b, a
    total = 0.0
    for i, av in a.items():
        if av == 0.0:
            continue
        bv = b.get(i)
        if bv is None or bv == 0.0:
            continue
        total += av * bv
    return total
