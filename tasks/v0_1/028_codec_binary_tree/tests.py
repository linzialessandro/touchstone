from solution import TreeNode, serialize, deserialize

def same(a, b):
    if a is None or b is None:
        return a is b
    return a.val == b.val and same(a.left, b.left) and same(a.right, b.right)

def main():
    assert same(deserialize(serialize(None)), None)
    t = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))
    assert same(deserialize(serialize(t)), t)
    t2 = TreeNode(1, None, TreeNode(2, None, TreeNode(3)))
    assert same(deserialize(serialize(t2)), t2)
    t3 = TreeNode(0, TreeNode(-1), None)
    assert same(deserialize(serialize(t3)), t3)
    print("OK")
if __name__=="__main__":
    main()
