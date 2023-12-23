class Node:
    def __init__(self, val):
        self.val = val
        self.rank = 0
        self.parent = self


def find(x):
    if x.val != x.parent.val:
        x.parent = find(x.parent)
    return x.parent


def union(x, y):
    root_x = find(x)
    root_y = find(y)

    if root_x == root_y:
        return

    if root_x.rank > root_y.rank:
        root_y.parent = root_x
    else:
        root_x.parent = root_y
        if root_x.rank == root_y.rank:
            root_x.rank += 1


def connected(x, y):
    return find(x) == find(y)


def test():
    nodes = [Node(val) for val in range(10)]
    union(nodes[1], nodes[2])
    union(nodes[2], nodes[3])
    union(nodes[1], nodes[4])

    union(nodes[8], nodes[9])
    union(nodes[7], nodes[8])

    assert connected(nodes[1], nodes[3])
    assert connected(nodes[1], nodes[9]) == False

    union(nodes[2], nodes[7])
    assert connected(nodes[1], nodes[9])