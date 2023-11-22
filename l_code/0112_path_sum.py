from node import Node


def path_sum(root, target_sum):
    def get_sum(root, target):
        if root.left is None and root.right is None:
            return target == root.val

        if root.left is None and root.right is not None:
            return get_sum(root.right, target - root.val)
        elif root.right is None and root.left is not None:
            return get_sum(root.left, target - root.val)

        return get_sum(root.left, target - root.val) or get_sum(root.right, target - root.val)

    if root is None:
        return False

    return get_sum(root, target_sum)


def test_success():
    a = Node(1)
    assert path_sum(a, 1) == True

    b = Node(2)

    a.left= b
    assert path_sum(a, 1) == False


