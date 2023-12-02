from node import get_balanced_bst, Node


# Time: O(N)  Space: O(log(H))
def is_balanced(root):
    def evaluate(node):
        if node is None:
            return True, -1

        is_balanced_left, h_left = evaluate(node.left)
        is_balanced_right, h_right = evaluate(node.right)
        is_balanced = is_balanced_left and is_balanced_right and abs(h_left - h_right) <= 1

        return is_balanced, max(h_left, h_right) + 1

    is_balanced, _ = evaluate(root)

    return is_balanced


def test():
    root = get_balanced_bst(14)
    assert is_balanced(root)

    n0, n1, n2, n3, n4, n5 = Node(), Node(), Node(), Node(), Node(), Node()
    n3.left, n3.right = n2, n4
    n2.left = n1
    n4.right = n5
    n1.left = n0
    assert is_balanced(n3) == False