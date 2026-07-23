# Touchstone hard task: merge accounts by shared emails (executable grading).
import kaggle_benchmarks as kbench

PROMPT = """You are solving a HARD coding task for the Touchstone benchmark.
Return a complete Python solution in one markdown fence (```python ... ```).
Include the full function. No omitted code.

# Merge accounts by shared emails

Implement:

```python
def merge_accounts(accounts: list[list[str]]) -> list[list[str]]:
    ...
```

## Spec

- Each account is `[name, email1, email2, ...]`.
- If two accounts share **any** email, they belong to the same person (same name in tests).
- Merge all emails for a person; output `[name, ...emails_sorted...]` per person.
- Output accounts sorted by name, then by first email.

## Example

Input:
[["John","j@x","j@y"],["John","j@y","j@z"],["Mary","m@x"]]

Output:
[["John","j@x","j@y","j@z"],["Mary","m@x"]]
"""


@kbench.task(
    name="ts-accounts-merge",
    description="Touchstone HARD: merge_accounts union-find style; executable asserts.",
)
def ts_accounts_merge(llm) -> bool:
    try:
        response = llm.prompt(PROMPT)
    except Exception:
        return False
    try:
        code = kbench.tools.python.extract_code(response)
    except Exception:
        return False
    if not code or "merge_accounts" not in code:
        return False
    prog = (
        code
        + """
acc = [
    ["John", "j@x", "j@y"],
    ["John", "j@y", "j@z"],
    ["Mary", "m@x"],
]
assert merge_accounts(acc) == [["John", "j@x", "j@y", "j@z"], ["Mary", "m@x"]]
assert merge_accounts([["A", "a@a"]]) == [["A", "a@a"]]
acc2 = [
    ["John", "a", "b"],
    ["John", "c"],
    ["John", "b", "d"],
]
assert merge_accounts(acc2) == [["John", "a", "b", "d"], ["John", "c"]]
print("OK")
"""
    )
    try:
        out = kbench.tools.python.script_runner.run_code(prog)
    except Exception:
        return False
    return out.exit_code == 0 and "OK" in (out.stdout or "")


ts_accounts_merge.run(kbench.llm)
