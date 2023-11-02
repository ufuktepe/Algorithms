def inorderTraversal(root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    stack = []
    if root is None:
        return stack

    vals = []

    while stack or root:
        while root:
            stack.append(root)
            root = root.left

        node = stack.pop()
        vals.append(node.val)
        root = node.right

    return vals