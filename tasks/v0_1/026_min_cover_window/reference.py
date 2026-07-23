def min_cover_window(s: str, need: dict[str, int]) -> str:
    if not need:
        return ""
    missing = sum(need.values())
    require = dict(need)
    have: dict[str, int] = {}
    best = ""
    best_len = float("inf")
    left = 0
    for right, ch in enumerate(s):
        if ch in require:
            have[ch] = have.get(ch, 0) + 1
            if have[ch] <= require[ch]:
                missing -= 1
        while missing == 0 and left <= right:
            if right - left + 1 < best_len:
                best_len = right - left + 1
                best = s[left : right + 1]
            left_ch = s[left]
            if left_ch in require:
                have[left_ch] -= 1
                if have[left_ch] < require[left_ch]:
                    missing += 1
            left += 1
    return best
