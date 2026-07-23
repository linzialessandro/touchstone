def normalize_path(path: str) -> str:
    absolute = path.startswith("/")
    parts: list[str] = []
    for seg in path.split("/"):
        if seg == "" or seg == ".":
            continue
        if seg == "..":
            if parts and parts[-1] != "..":
                parts.pop()
            elif not absolute:
                parts.append("..")
            # absolute at root: ignore ..
            continue
        parts.append(seg)
    if not parts:
        return "/" if absolute else "."
    body = "/".join(parts)
    return "/" + body if absolute else body
