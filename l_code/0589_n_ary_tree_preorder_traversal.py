from node import NaryNode


# Time: O(N)  Space: O(N)
def preorder_rec(root):
    res = []

    def traverse(node):
        if node is None:
            return

        res.append(node.val)

        for child in node.children:
            traverse(child)

    traverse(root)
    return res


# Time: O(N)  Space: O(N)
def preorder_iter(root):
    if root is None:
        return root
    res = []
    stack = [root]

    while stack:
        node = stack.pop()
        res.append(node.val)

        for child in node.children[::-1]:
            stack.append(child)
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


def test_rec():
    n1 = get_nary_tree()
    assert preorder_rec(n1) == [1, 3, 5, 6, 2, 4]


def test_iter():
    n1 = get_nary_tree()
    assert preorder_iter(n1) == [1, 3, 5, 6, 2, 4]