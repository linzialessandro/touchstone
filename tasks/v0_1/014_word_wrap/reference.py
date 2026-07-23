def word_wrap(text: str, width: int) -> list[str]:
    if width < 1:
        raise ValueError("width")
    words = text.split()
    if not words:
        return []
    for w in words:
        if len(w) > width:
            raise ValueError("word too long")
    lines: list[str] = []
    cur: list[str] = []
    cur_len = 0
    for w in words:
        add = len(w) if not cur else len(w) + 1
        if cur_len + add <= width:
            cur.append(w)
            cur_len += add
        else:
            lines.append(" ".join(cur))
            cur = [w]
            cur_len = len(w)
    if cur:
        lines.append(" ".join(cur))
    return lines
