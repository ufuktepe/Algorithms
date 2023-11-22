from collections import deque

from node import Node


def generate_trees(n):
    cache = {}

    def generate(start, end):
        if start > end:
            return [None]

        if (start, end) in cache:
            return cache[(start, end)]

        trees = []
        for i in range(start, end + 1):
            left_trees = generate(start, i - 1)
            right_trees = generate(i + 1, end)

            for left_node in left_trees:
                for right_node in right_trees:
                    root = Node(i, left=left_node, right=right_node)
                    trees.append(root)

        cache[(start, end)] = trees
        return cache[(start, end)]

    generate(1, n)
    return cache[(1, n)]


def test():
    trees = generate_trees(3)
    solution = {(1, 3, 2), (1, 2, 3), (2, 1, 3), (3, 2, 1), (3, 1, 2)}

    for tree in trees:
        serialized = serialize_tree(tree)
        assert serialized in solution


def serialize_tree(tree):
    serialized = []
    q = deque([tree])

    while q:
        node = q.popleft()
        serialized.append(node.val)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)

    return tuple(serialized)

