from node import Node


# Time: O(log(N))  Space: O(log(N)) to keep the recursion stack
def search_bst_rec(root, val):
    if root is None:
        return None

    if root.val == val:
        return root
    elif val < root.val:
        return search_bst_rec(root.left, val)
    else:
        return search_bst_rec(root.right, val)


# Time: O(log(N))  Space: O(1)
def search_bst_iter(root, val):
    cur = root

    while cur:
        if cur.val == val:
            return cur
        elif val < cur.val:
            cur = cur.left
        else:
            cur = cur.right

    return None

def test():
    a = Node(10)
    b = Node(5)
    c = Node(15)
    d = Node(0)
    e = Node(7)
    f = Node(12)
    g = Node(20)

    a.left, a.right = b, c
    b.left, b.right = d, e
    c.left, c.right = f, g

    assert search_bst_iter(a, 20) == g
    assert search_bst_iter(a, 19) is None