from collections import deque
from node import get_balanced_bst


# Time: O(n)  Space: O(n)
def binary_tree_width(root):
    q = deque([(root, 0)])
    width = 0

    while q:
        next_level = deque()
        n = len(q)
        left, right = None, None

        for i in range(n):
            node, idx = q.popleft()

            if node.left:
                next_level.append((node.left, 2 * idx + 1))
            if node.right:
                next_level.append((node.right, 2 * idx + 2))

            if left is None:
                left = idx
            right = idx

        width = max(width, right - left + 1)
        q = next_level

    return width


def test():
    root = get_balanced_bst(6)
    assert binary_tree_width(root) == 3


def test_2():
    root = get_balanced_bst(1)
    assert binary_tree_width(root) == 1