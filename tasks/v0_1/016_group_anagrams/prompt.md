# Group anagrams

Implement:

```python
def group_anagrams(words: list[str]) -> list[list[str]]:
    ...
```

## Spec

- Two words are anagrams if they contain the same multiset of characters (case-sensitive).
- Group words into lists of mutual anagrams.
- Within each group, preserve **input order**.
- Groups themselves are ordered by the **first occurrence** of any member in the input.
- Empty string is a valid word.

## Example

`["eat","tea","tan","ate","nat","bat"]` →
`[["eat","tea","ate"],["tan","nat"],["bat"]]`
