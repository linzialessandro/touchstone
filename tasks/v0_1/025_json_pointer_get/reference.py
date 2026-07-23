def pointer_get(doc: object, pointer: str) -> object:
    if pointer == "":
        return doc
    if not pointer.startswith("/"):
        raise KeyError("pointer must start with /")
    cur: object = doc
    # split keeps empty first element before leading /
    tokens = pointer.split("/")[1:]
    for tok in tokens:
        if isinstance(cur, list):
            if tok != "0" and (tok.startswith("0") or not tok.isdigit()):
                raise KeyError(tok)
            if not tok.isdigit():
                raise KeyError(tok)
            idx = int(tok)
            if idx < 0 or idx >= len(cur):
                raise KeyError(tok)
            cur = cur[idx]
        elif isinstance(cur, dict):
            if tok not in cur:
                raise KeyError(tok)
            cur = cur[tok]
        else:
            raise KeyError(tok)
    return cur
