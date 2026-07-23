# Serialize and deserialize binary tree

Implement:

```python
class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode | None" = None, right: "TreeNode | None" = None):
        self.val = val
        self.left = left
        self.right = right

def serialize(root: TreeNode | None) -> str: ...
def deserialize(data: str) -> TreeNode | None: ...
```

## Spec

- Round-trip: `deserialize(serialize(root))` equals the original tree structurally.
- Encoding format is **your choice**, but must be a single string.
- Empty tree ↔ a defined encoding of your choice (tests only check round-trip and a few fixed shapes via values).
- Node values are integers.

Tests build trees and check values via level-order including null structure.
