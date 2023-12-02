from node import NaryNode


# Time: O(N)  Space: O(N)
def postorder_rec(root):
    res = []

    def traverse(node):
        if node is None:
            return

        for child in node.children:
            traverse(child)

        res.append(node.val)

    traverse(root)
    return res


# Time: O(N)  Space: O(N)
def postorder_iter(root):
    if root is None:
        return root

    res = []

    stack = [(root, False)]

    while stack:
        node, visited = stack.pop()

        if visited:
            res.append(node.val)
        else:
            stack.append((node, True))

            for child in node.children[::-1]:
                stack.append((child, False))
    return res


def get_nary_tree():
    n1 = NaryNode(1)
    n2 = NaryNode(2)
    n3 = NaryNode(3)
    n4 = NaryNode(4)
    n5 = NaryNode(5)
    n6 = NaryNode(6)

    n1.children = [n3, n2, n4]
    n3.children = [n5, n6]

    return n1


def test_postorder_rec():
    n1 = get_nary_tree()
    assert postorder_rec(n1) == [5, 6, 3, 2, 4, 1]


def test_postorder_iter():
    n1 = get_nary_tree()
    assert postorder_iter(n1) == [5, 6, 3, 2, 4, 1]