def rle_encode(s: str) -> str:
    if not s:
        return ""
    if any(c < "A" or c > "Z" for c in s):
        raise ValueError("invalid char")
    out: list[str] = []
    i = 0
    n = len(s)
    while i < n:
        j = i
        while j < n and s[j] == s[i]:
            j += 1
        out.append(s[i])
        cnt = j - i
        if cnt >= 2:
            out.append(str(cnt))
        i = j
    return "".join(out)
