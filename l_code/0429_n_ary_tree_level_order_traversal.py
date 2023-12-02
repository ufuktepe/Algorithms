from collections import deque

from node import NaryNode


# Time: O(N)  Space: O(N)
def levelorder(root):
    if root is None:
        return root

    res = []
    q = deque([[root]])

    while q:
        nodes = q.popleft()
        vals = []
        next_level_nodes = []

        for node in nodes:
            vals.append(node.val)

            for child in node.children:
                next_level_nodes.append(child)

        res.append(vals)
        if next_level_nodes:
            q.append(next_level_nodes)

    return res


def test():
    n1 = NaryNode(1)
    n2 = NaryNode(2)
    n3 = NaryNode(3)
    n4 = NaryNode(4)
    n5 = NaryNode(5)
    n6 = NaryNode(6)
    n7 = NaryNode(7)
    n8 = NaryNode(8)
    n9 = NaryNode(9)

    n1.children = [n2, n3, n4]
    n2.children = [n5]
    n3.children = [n6, n7]
    n4.children = [n8, n9]

    assert levelorder(n1) == [[1], [2, 3, 4], [5, 6, 7, 8, 9]]

