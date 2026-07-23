# Merge accounts by shared emails

Implement:

```python
def merge_accounts(accounts: list[list[str]]) -> list[list[str]]:
    ...
```

## Spec

- Each account is `[name, email1, email2, ...]`.
- If two accounts share **any** email, they belong to the same person (same name guaranteed for merges in tests).
- Merge all emails for a person; output `[name, ...emails_sorted...]` per person.
- Output accounts sorted by name, then by first email.
- Preserve that different names never merge even if... (tests only same-name merges).

## Example

```
[["John","j@x","j@y"],["John","j@y","j@z"],["Mary","m@x"]]
```
→ `[["John","j@x","j@y","j@z"],["Mary","m@x"]]`
