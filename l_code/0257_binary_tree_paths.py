from node import get_balanced_bst, Node


# Time: O(Nlog(N))  Space: O(Nlog(N))
def get_paths(root):
    def traverse(node):
        if node is None:
            return []

        if node.left is None and node.right is None:
            return [[str(node.val)]]

        left_paths = traverse(node.left)
        right_paths = traverse(node.right)

        paths = []

        for path in left_paths:
            path.append(str(node.val))
            paths.append(path)

        for path in right_paths:
            path.append(str(node.val))
            paths.append(path)

        return paths

    all_paths = traverse(root)
    res = []
    for path in all_paths:
        res.append('->'.join(path[::-1]))

    return res


def test_1_node():
    root = Node(1)
    assert get_paths(root) == ['1']


def test_2_nodes():
    root = get_balanced_bst(2)
    assert get_paths(root) == ['1->2']


def test_7_nodes():
    root = get_balanced_bst(7)
    assert get_paths(root) == ['4->2->1', '4->2->3', '4->6->5', '4->6->7']
