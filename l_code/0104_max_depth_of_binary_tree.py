class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_depth(root):
    def get_depth(root, depth):
        if root is None:
            return depth
        return max(get_depth(root.left, depth + 1), get_depth(root.right, depth + 1))

    return get_depth(root, 0)


def test_1():
    a = Node('a')
    b = Node('b')
    a.left = b
    assert max_depth(a) == 2