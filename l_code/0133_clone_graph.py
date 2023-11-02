
class Node(object):
    def __init__(self, val=0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def clone_graph(node):
    """
    :type node: Node
    :rtype: Node
    """
    copy = {}
    if node is None:
        return
    dfs(node, copy)
    return copy[node.val]


def dfs(node, copy):
    copy[node.val] = Node(val=node.val)
    for nbr in node.neighbors:
        if nbr.val not in copy:
            dfs(nbr, copy)

        copy[node.val].neighbors.append(copy[nbr.val])


def test_clone_graph():
    a = Node(val=1)
    b = Node(val=2)
    c = Node(val=3)
    d = Node(val=4)

    a.neighbors = [c, b]
    b.neighbors = [a, d]
    c.neighbors = [a, d]
    d.neighbors = [b, c]

    assert clone_graph(a).val == 1
