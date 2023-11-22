from node import Node


class TreeNode(Node):
    def __init__(self, val):
        super().__init__(val)
        self.next = None


# Time: O(N)  Space: O(N)
def connect(root):
    next_level = [root]

    while next_level:
        curr_level = next_level
        next_level = []

        for i, node in enumerate(curr_level):
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)

            if i + 1 < len(curr_level):
                node.next = curr_level[i + 1]


# Time: O(N)  Space: O(1)
def connect_v2(root):
    head = root

    while head.left:
        cur = head

        while cur:
            cur.left.next = cur.right
            if cur.next:
                cur.right.next = cur.next.left
            cur = cur.next

        head = head.left


# Time: O(N)  Space: O(1)
def connect_dfs(root):
    if root is None:
        return
    if root.left:
        root.left.next = root.right
        if root.next:
            root.right.next = root.next.left
        connect_dfs(root.left)
        connect_dfs(root.right)


def test_1():
    a = TreeNode('a')
    b = TreeNode('b')
    c = TreeNode('c')
    d = TreeNode('d')
    e = TreeNode('e')
    f = TreeNode('f')
    g = TreeNode('g')

    a.left, a.right = b, c
    b.left, b.right = d, e
    c.left, c.right = f, g

    connect_dfs(a)

    assert a.next is None
    assert b.next == c
    assert c.next is None
    assert d.next == e
    assert e.next == f
    assert f.next == g
    assert g.next is None
