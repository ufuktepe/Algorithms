def delete_node(root, key):
    if root is None:
        return None

    if root.val > key:
        root.left = delete_node(root.left, key)
    elif root.val < key:
        root.right = delete_node(root.right, key)
    else:
        # Delete this root
        if root.right is None:
            root = root.left
        elif root.left is None:
            root = root.right
        else:
            predecessor = root.left
            while predecessor.right:
                predecessor = predecessor.right
            root.val = predecessor.val
            root.left = delete_node(root.left, root.val)

    return root
