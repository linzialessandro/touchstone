class TreeNode:
    def __init__(self, val: int = 0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(root: TreeNode | None) -> str:
    out: list[str] = []
    def dfs(node):
        if node is None:
            out.append("#")
            return
        out.append(str(node.val))
        dfs(node.left)
        dfs(node.right)
    dfs(root)
    return ",".join(out)

def deserialize(data: str) -> TreeNode | None:
    if data == "":
        return None
    parts = iter(data.split(","))
    def dfs():
        val = next(parts)
        if val == "#":
            return None
        node = TreeNode(int(val))
        node.left = dfs()
        node.right = dfs()
        return node
    return dfs()
