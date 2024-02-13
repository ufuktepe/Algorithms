from collections import deque
from node import get_balanced_bst


# Time: O(n)  Space: O(n)
def right_side_view(root):
    q = deque([root])
    res = []

    while q:
        n = len(q)
        last = None

        for i in range(n):
            node = q.popleft()
            last = node

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        res.append(last.val)
    return res


def test():
    root = get_balanced_bst(5)
    assert right_side_view(root) == [3, 4, 5]