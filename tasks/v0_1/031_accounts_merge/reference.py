def merge_accounts(accounts: list[list[str]]) -> list[list[str]]:
    parent: dict[str, str] = {}
    email_name: dict[str, str] = {}

    def find(x: str) -> str:
        parent.setdefault(x, x)
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a: str, b: str) -> None:
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[rb] = ra

    for acc in accounts:
        name = acc[0]
        emails = acc[1:]
        if not emails:
            continue
        first = emails[0]
        for e in emails:
            email_name[e] = name
            union(first, e)

    groups: dict[str, list[str]] = {}
    for e in email_name:
        root = find(e)
        groups.setdefault(root, []).append(e)

    out: list[list[str]] = []
    for root, emails in groups.items():
        name = email_name[root]
        out.append([name] + sorted(set(emails)))
    out.sort(key=lambda row: (row[0], row[1]))
    return out
