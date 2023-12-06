def is_identical(p, q):
    stack = [(p, q)]

    while stack:
        root1, root2 = stack.pop()

        if root1 is None and root2 is None:
            continue

        if root1 is None or root2 is None:
            return False

        if root1.val != root2.val:
            return False

        stack.append((root1.left, root2.left))
        stack.append((root1.right, root2.right))

    return True