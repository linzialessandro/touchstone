# Parse INI-like sections

Implement:

```python
def parse_ini_sections(text: str) -> dict[str, dict[str, str]]:
    ...
```

## Mini-spec (read carefully)

1. Input is a multi-line string.
2. Lines that are empty or only whitespace are ignored.
3. Lines starting with `#` or `;` (after stripping) are comments; ignore them.
4. A section header is a line of the form `[name]` after strip. `name` is the stripped inside of the brackets. Create the section if new.
5. Key/value lines contain `=`. Split on the **first** `=`. Strip key and value. Assign into the **current** section.
6. Key/value lines **before any section** are ignored.
7. If a line is not a comment, not a section, and has no `=`, ignore it.
8. Duplicate keys in the same section: **last write wins**.
9. Return type: `dict[str, dict[str, str]]` mapping section name → key → value.
10. Do not use `configparser` (implement the rules above yourself).

## Example

```ini
# global comment
[database]
host = localhost
port = 5432

[database]
user = alice

[cache]
; disabled
enabled = true
```

Result shape:

```python
{
  "database": {"host": "localhost", "port": "5432", "user": "alice"},
  "cache": {"enabled": "true"},
}
```
