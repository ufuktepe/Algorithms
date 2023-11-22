def postorder_traversal(root):
    if root is None:
        return []

    res = []
    stack = [(root, False)]

    while stack:
        node, visited = stack.pop()

        if visited:
            res.append(node.val)
        else:
            stack.append((node, True))
            if node.right:
                stack.append((node.right, False))
            if node.left:
                stack.append((node.left, False))
    return res