from collections import OrderedDict

def group_anagrams(words: list[str]) -> list[list[str]]:
    groups: OrderedDict[tuple[str, ...], list[str]] = OrderedDict()
    for w in words:
        key = tuple(sorted(w))
        groups.setdefault(key, []).append(w)
    return list(groups.values())
