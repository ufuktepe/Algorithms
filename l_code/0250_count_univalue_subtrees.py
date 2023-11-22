from node import Node


def count_univalue_subtrees(root):
    def get_subtree_info(root):
        if root is None:
            return 0, True
        if root.left is None and root.right is None:
            return 1, True

        count_left, is_univalue_left = get_subtree_info(root.left)
        count_right, is_univalue_right = get_subtree_info(root.right)

        is_univalue = is_univalue_left and is_univalue_right
        if root.left and root.left.val != root.val:
            is_univalue = False
        if root.right and root.right.val != root.val:
            is_univalue = False

        count = count_left + count_right

        if is_univalue:
            count += 1

        return count, is_univalue

    count, _ = get_subtree_info(root)
    return count


def test_1():
    a = Node(5)
    b = Node(5)
    c = Node(5)
    d = Node(5)

    a.left, a.right = b, c
    c.left = d

    assert count_univalue_subtrees(a) == 4