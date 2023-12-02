from node import get_balanced_bst


# Time: O(H)  Space: O(H) where H is the height of the BST
def search_bst_rec(root, val):
    if root is None:
        return root
    if root.val == val:
        return root
    if root.val > val:
        return search_bst_rec(root.left, val)
    else:
        return search_bst_rec(root.right, val)


# Time: O(H)  Space: O(1) where H is the height of the BST
def search_bst_iter(root, val):
    while root:
        if root.val == val:
            return root
        if root.val > val:
            root = root.left
        else:
            root = root.right
    return None


def test():
    root = get_balanced_bst(7)
    assert search_bst_rec(root, 3).val == 3
    assert search_bst_iter(root, 3).val == 3

    assert search_bst_rec(root, 13) == None
    assert search_bst_iter(root, 13) == None