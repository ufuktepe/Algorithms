from node import get_balanced_bst


# Time: O(log(H))  Space: O(log(H))
def find_lca(root, p, q):
    def get_lca(root, a, b):
        if root.val < a.val:
            return get_lca(root.right, a, b)
        elif a.val <= root.val <= b.val:
            return root
        else:
            return get_lca(root.left, a, b)

    if p.val < q.val:
        return get_lca(root, p, q)
    else:
        return get_lca(root, q, p)


def test():
    root = get_balanced_bst(15)

    assert find_lca(root, root.left, root.right) == root