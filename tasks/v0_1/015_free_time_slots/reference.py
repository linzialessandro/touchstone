def free_slots(busy: list[tuple[int, int]], day_start: int, day_end: int) -> list[tuple[int, int]]:
    if day_start >= day_end:
        return []
    clipped: list[tuple[int, int]] = []
    for s, e in busy:
        if s >= e:
            continue
        s2 = max(s, day_start)
        e2 = min(e, day_end)
        if s2 < e2:
            clipped.append((s2, e2))
    clipped.sort()
    merged: list[tuple[int, int]] = []
    for s, e in clipped:
        if not merged or s > merged[-1][1]:
            merged.append((s, e))
        else:
            merged[-1] = (merged[-1][0], max(merged[-1][1], e))
    free: list[tuple[int, int]] = []
    cur = day_start
    for s, e in merged:
        if cur < s:
            free.append((cur, s))
        cur = max(cur, e)
    if cur < day_end:
        free.append((cur, day_end))
    return free
