def merge_labeled(intervals: list[tuple[int, int, str]]) -> list[tuple[int, int, str]]:
    cleaned = [(s, e, lab) for s, e, lab in intervals if s <= e]
    cleaned.sort(key=lambda t: (t[0], t[1], t[2]))
    # Merge per label independently, then re-sort
    by_lab: dict[str, list[tuple[int, int]]] = {}
    for s, e, lab in cleaned:
        by_lab.setdefault(lab, []).append((s, e))
    out: list[tuple[int, int, str]] = []
    for lab, ivs in by_lab.items():
        ivs.sort()
        cur_s, cur_e = ivs[0]
        for s, e in ivs[1:]:
            if s <= cur_e + 1:
                cur_e = max(cur_e, e)
            else:
                out.append((cur_s, cur_e, lab))
                cur_s, cur_e = s, e
        out.append((cur_s, cur_e, lab))
    out.sort(key=lambda t: (t[0], t[1], t[2]))
    return out
