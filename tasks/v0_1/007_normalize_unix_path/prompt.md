# Normalize a Unix-style path

Implement:

```python
def normalize_path(path: str) -> str:
    ...
```

## Spec

1. Split `path` on `/`. Empty segments from repeated slashes are ignored.
2. `.` segments are ignored.
3. `..` pops the previous segment if one exists; if at root of a relative path with nothing to pop, keep a leading `..` for relative paths.
4. If the original path starts with `/`, the result is absolute (starts with `/`).
5. If the result has no segments: return `"/"` for absolute, `"."` for relative.
6. Do not resolve symlinks; string rules only.
7. Trailing slash is not preserved.

## Examples

- `"/a/./b/../c/"` → `"/a/c"`
- `"a/b/../../c"` → `"c"`
- `""` or `"."` → `"."`
- `"/../a"` → `"/a"` (absolute: `..` at root is ignored)
- `"../a/b"` → `"../a/b"`
