def cmp_version(a: str, b: str) -> int:
    def parse(v: str) -> list[int]:
        if v == "" or v.startswith(".") or v.endswith(".") or ".." in v:
            raise ValueError(f"invalid version: {v!r}")
        parts = v.split(".")
        out: list[int] = []
        for p in parts:
            if p == "" or not p.isdigit():
                raise ValueError(f"invalid segment: {p!r}")
            out.append(int(p))
        return out

    pa, pb = parse(a), parse(b)
    n = max(len(pa), len(pb))
    pa.extend([0] * (n - len(pa)))
    pb.extend([0] * (n - len(pb)))
    for x, y in zip(pa, pb):
        if x < y:
            return -1
        if x > y:
            return 1
    return 0
