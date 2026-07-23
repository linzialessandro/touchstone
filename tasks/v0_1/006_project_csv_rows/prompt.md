# Project CSV-like rows

Implement:

```python
def project_rows(text: str, columns: list[str]) -> list[dict[str, str]]:
    ...
```

## Spec

1. Split `text` into lines; strip each line; skip empty lines.
2. First non-empty line is the **header**: comma-separated column names (strip each name).
3. Subsequent lines are data rows: comma-separated fields (strip each field).
4. If a data row has a **different number of fields** than the header, **skip** that row.
5. For each kept row, build a dict mapping header name → field value.
6. Return a list of dicts containing **only** keys listed in `columns` (in that order of keys is not required; missing requested columns are omitted if not in header).
7. If a name in `columns` is not in the header, ignore that name.
8. No CSV quoting rules: commas always split (simple dialect).

## Example

Text:
```
name,age,city
ann,30,rome
bob,badrow
cara,25,milan
```
`columns=["city","name"]` → `[{"city":"rome","name":"ann"}, {"city":"milan","name":"cara"}]`
