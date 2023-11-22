from node import Node


def lowest_common_ancestor(root, p, q):
    parent = {root: None}

    def populate_parent(node):
        if node.left:
            parent[node.left] = node
            populate_parent(node.left)

        if node.right:
            parent[node.right] = node
            populate_parent(node.right)

    populate_parent(root)

    path_p = {}  # maps values to nodes

    cur = p
    while cur:
        path_p[cur.val] = cur
        cur = parent[cur]

    cur = q
    while cur:
        if cur.val in path_p:
            return path_p[cur.val]
        cur = parent[cur]


def test_1():
    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    e = Node('e')
    f = Node('f')
    g = Node('g')

    a.left, a.right = b, c
    b.left, b.right = d, e
    c.left, c.right = f, g

    assert lowest_common_ancestor(a, d, f) == a
