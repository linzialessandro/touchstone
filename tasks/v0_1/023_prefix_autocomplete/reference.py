def autocomplete(words: list[str], prefix: str, k: int) -> list[str]:
    if k <= 0:
        return []
    matches = [w for w in words if w.startswith(prefix)]
    matches.sort()
    return matches[:k]
