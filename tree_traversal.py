from collections import deque


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def preorder_rec(root):
    res = []

    def traverse(node):
        if node is None:
            return
        res.append(node.val)
        traverse(node.left)
        traverse(node.right)

    traverse(root)
    return res


def preorder_iter(root):
    res = []
    stack = [root]

    while stack:
        node = stack.pop()
        res.append(node.val)

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return res


def inorder_rec(root):
    res = []

    def traverse(node):
        if node is None:
            return
        traverse(node.left)
        res.append(node.val)
        traverse(node.right)

    traverse(root)
    return res


def inorder_iter(root):
    res = []
    stack = []
    node = root

    while stack or node:
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            res.append(node.val)
            node = node.right
    return res


def inorder_dfs_iter(root):
    res = []
    stack = [(root, False)]

    while stack:
        node, visited = stack.pop()

        if visited:
            res.append(node.val)
        else:
            if node.right:
                stack.append((node.right, False))
            stack.append((node, True))
            if node.left:
                stack.append((node.left, False))
    return res


def postorder_rec(root):
    res = []

    def traverse(node):
        if node is None:
            return
        traverse(node.left)
        traverse(node.right)
        res.append(node.val)

    traverse(root)
    return res


def postorder_dfs_iter(root):
    res = []
    stack = [(root, False)]

    while stack:
        node, visited = stack.pop()

        if visited:
            res.append(node.val)
        else:
            stack.append((node, True))
            if node.right:
                stack.append((node.right, False))
            if node.left:
                stack.append((node.left, False))

    return res


def level_order_traversal_iter(root):
    res = []
    queue = deque([root])

    while queue:
        res.append([])
        num_of_nodes = len(queue)  # Number of nodes in this level

        for i in range(num_of_nodes):
            node = queue.popleft()
            res[-1].append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return res


def level_order_traversal_rec(root):
    res = []

    def traverse(node, level):
        if node is None:
            return
        if level == len(res):
            res.append([])
        res[level].append(node.val)

        traverse(node.left, level + 1)
        traverse(node.right, level + 1)

    traverse(root, 0)

    return res


#        D
#      /   \
#     C     F
#    /     / \
#   A     E   H
#    \       /
#     B     G
def get_tree():
    a = Node('A')
    b = Node('B')
    c = Node('C')
    d = Node('D')
    e = Node('E')
    f = Node('F')
    g = Node('G')
    h = Node('H')

    a.right = b
    c.left = a
    h.left = g
    f.left, f.right = e, h
    d.left, d.right = c, f

    return d


def test_preorder():
    root = get_tree()
    assert preorder_rec(root) == ['D', 'C', 'A', 'B', 'F', 'E', 'H', 'G']
    assert preorder_iter(root) == ['D', 'C', 'A', 'B', 'F', 'E', 'H', 'G']


def test_inorder_rec():
    root = get_tree()
    assert inorder_rec(root) == ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    assert inorder_iter(root) == ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    assert inorder_dfs_iter(root) == ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']


def test_postorder_rec():
    root = get_tree()
    assert postorder_rec(root) == ['B', 'A', 'C', 'E', 'G', 'H', 'F', 'D']
    assert postorder_dfs_iter(root) == ['B', 'A', 'C', 'E', 'G', 'H', 'F', 'D']


def test_level_order_traversal():
    root = get_tree()
    assert level_order_traversal_iter(root) == [['D'], ['C', 'F'], ['A', 'E', 'H'], ['B', 'G']]
    assert level_order_traversal_rec(root) == [['D'], ['C', 'F'], ['A', 'E', 'H'], ['B', 'G']]