from collections import deque
from node import get_balanced_bst, get_inorder_vals


# Time: O(n)  Space: O(h)
def invert(root):
    if root is None:
        return None

    left_root = root.left
    root.left = invert(root.right)
    root.right = invert(left_root)

    return root


# Time: O(n)  Space: O(n)
def invert_iter(root):
    if root is None:
        return None

    q = deque([root])

    while q:
        node = q.popleft()
        node.left, node.right = node.right, node.left
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)

    return root



def test():
    root = get_balanced_bst(3)
    new_root = invert_iter(root)
    inorder_vals = get_inorder_vals(new_root)
    assert inorder_vals == [3, 2, 1]


def test_2():
    root = get_balanced_bst(5)
    new_root = invert_iter(root)
    inorder_vals = get_inorder_vals(new_root)
    assert inorder_vals == [5, 4, 3, 2, 1]