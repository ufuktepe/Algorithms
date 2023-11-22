from node import Node


# Time: O(N)  Space: O(N)
def build_tree(preorder, inorder):
    idx_map = {val: i for i, val in enumerate(inorder)}
    preorder_idx = 0

    def traverse(left_idx, right_idx):
        nonlocal preorder_idx

        if not 0 <= preorder_idx < len(preorder):
            return None

        curr_val = preorder[preorder_idx]
        curr_idx = idx_map[curr_val]  # inorder index of current value

        if not left_idx <= curr_idx <= right_idx:
            return None

        preorder_idx += 1
        root = Node(curr_val)
        root.left = traverse(left_idx, curr_idx - 1)
        root.right = traverse(curr_idx + 1, right_idx)

        return root

    return traverse(0, len(inorder) - 1)


def is_identical(root1, root2):
    if root1 is None and root2 is None:
        return True
    if root1 is None or root2 is None or root1.val != root2.val:
        return False

    if not is_identical(root1.left, root2.left):
        return False
    if not is_identical(root1.right, root2.right):
        return False

    return True


def test_1():
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n6 = Node(6)
    n7 = Node(7)
    n8 = Node(8)
    n9 = Node(9)

    n3.left = n2
    n4.left, n4.right = n3, n5
    n7.right = n8
    n1.right = n4
    n9.left = n7
    n6.left, n6.right = n1, n9

    preorder = [6, 1, 4, 3, 2, 5, 9, 7, 8]
    inorder = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    root = build_tree(preorder, inorder)

    assert is_identical(n6, root)