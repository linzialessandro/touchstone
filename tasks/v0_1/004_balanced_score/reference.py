def balanced_score(s: str) -> int:
    stack: list[str] = []
    score = 0
    for ch in s:
        if ch in "([":
            stack.append(ch)
        elif ch == ")":
            if not stack or stack[-1] != "(":
                return -1
            stack.pop()
            score += 1
        elif ch == "]":
            if not stack or stack[-1] != "[":
                return -1
            stack.pop()
            score += 2
    if stack:
        return -1
    return score
