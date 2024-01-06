from node import get_balanced_bst


# Time: O(k)  Space: O(k)
def get_kth_smallest(root, k):
    if root is None:
        return

    res = []

    def traverse(node):
        if node is None:
            return

        traverse(node.left)

        if len(res) == k:
            return
        res.append(node.val)

        traverse(node.right)

    traverse(root)
    return res[-1]


def test():
    root = get_balanced_bst(10)
    assert get_kth_smallest(root, 10) == 10