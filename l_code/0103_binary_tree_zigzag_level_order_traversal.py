from node import get_balanced_bst


# Time: O(n)  Space: O(n)
def zigzag_level_order(root):
    if root is None:
        return []

    stack = [root]
    level = 0
    res = []

    while stack:
        n = len(stack)
        next_stack = []
        cur_level_node_vals = []

        for i in range(n):
            node = stack.pop()
            cur_level_node_vals.append(node.val)
            if level % 2 == 0:
                if node.left:
                    next_stack.append(node.left)
                if node.right:
                    next_stack.append(node.right)
            else:
                if node.right:
                    next_stack.append(node.right)
                if node.left:
                    next_stack.append(node.left)

        res.append(cur_level_node_vals)
        level += 1
        stack = next_stack

    return res


def test():
    root = get_balanced_bst(1)
    assert zigzag_level_order(root) == [[1]]


def test_2():
    root = get_balanced_bst(2)
    assert zigzag_level_order(root) == [[1], [2]]


def test_3():
    root = get_balanced_bst(3)
    assert zigzag_level_order(root) == [[2], [3, 1]]


def test_4():
    root = get_balanced_bst(7)
    assert zigzag_level_order(root) == [[4], [6, 2], [1, 3, 5, 7]]