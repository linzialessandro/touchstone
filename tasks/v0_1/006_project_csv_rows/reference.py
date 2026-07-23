def project_rows(text: str, columns: list[str]) -> list[dict[str, str]]:
    lines = [ln.strip() for ln in text.splitlines() if ln.strip()]
    if not lines:
        return []
    header = [h.strip() for h in lines[0].split(",")]
    wanted = [c for c in columns if c in header]
    idx = {name: i for i, name in enumerate(header)}
    out: list[dict[str, str]] = []
    for line in lines[1:]:
        fields = [f.strip() for f in line.split(",")]
        if len(fields) != len(header):
            continue
        row = {c: fields[idx[c]] for c in wanted}
        out.append(row)
    return out
