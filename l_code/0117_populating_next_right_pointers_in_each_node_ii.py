from node import Node


class TreeNode(Node):
    def __init__(self, val):
        super().__init__(val)
        self.next = None


def connect(root):
    if root is None:
        return

    if root.left:
        if root.right:
            root.left.next = root.right
        else:
            cur = root.next

            while cur:
                if cur.left:
                    root.left.next = cur.left
                    break
                if cur.right:
                    root.left.next = cur.right
                    break
                cur = cur.next


    if root.right:
        cur = root.next

        while cur:
            if cur.left:
                root.right.next = cur.left
                break
            if cur.right:
                root.right.next = cur.right
                break
            cur = cur.next

    connect(root.right)
    connect(root.left)


    return root


def test_1():
    a = TreeNode(2)
    b = TreeNode(1)
    c = TreeNode(3)
    d = TreeNode(0)
    e = TreeNode(7)
    f = TreeNode(9)
    g = TreeNode(1)
    h = TreeNode(2)
    i = TreeNode(1)
    j = TreeNode(0)
    k = TreeNode(8)
    m = TreeNode(8)
    n = TreeNode(7)

    a.left, a.right = b, c
    b.left, b.right = d, e
    c.left, c.right = f, g
    d.left = h
    e.left, e.right = i, j
    g.left, g.right = k, m

    connect(a)

    assert b.next == c
    assert d.next == e
    assert e.next == f
    assert f.next == g
    assert h.next == i
    assert i.next == j
    assert j.next == k
    assert k.next == m
