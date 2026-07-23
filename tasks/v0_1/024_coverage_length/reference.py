def coverage_length(intervals: list[tuple[int, int]]) -> int:
    cleaned = sorted((s, e) for s, e in intervals if s < e)
    if not cleaned:
        return 0
    total = 0
    cs, ce = cleaned[0]
    for s, e in cleaned[1:]:
        if s > ce:
            total += ce - cs
            cs, ce = s, e
        else:
            ce = max(ce, e)
    total += ce - cs
    return total
