from node import get_balanced_bst


# Time: O(n)  Space: O(n)
def get_dia(root):
    def traverse(node):
        if node is None:
            return 0, 0
        height_left, dia_left = traverse(node.left)
        height_right, dia_right = traverse(node.right)

        cur_dia = height_left + height_right

        return max(height_left, height_right) + 1, max(cur_dia, dia_left, dia_right)

    _, dia = traverse(root)

    return dia


def test():
    root = get_balanced_bst(3)
    assert get_dia(root) == 2


def test_2():
    root = get_balanced_bst(1)
    assert get_dia(root) == 0


def test_3():
    root = get_balanced_bst(7)
    assert get_dia(root) == 4