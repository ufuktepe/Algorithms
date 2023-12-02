from node import NaryNode


# Time: O(N)  Space: O(N) due to recursion
def max_depth_rec(root):
    if root is None:
        return 0

    def get_depth(node, depth):
        maximum_depth = depth
        for child in node.children:
            maximum_depth = max(maximum_depth, get_depth(child, depth + 1))
        return maximum_depth

    return get_depth(root, 1)


# Time: O(N)  Space: O(N)
def max_depth_iter(root):
    if root is None:
        return 0

    stack = [(root, 1)]
    max_depth = 0

    while stack:
        node, depth = stack.pop()
        max_depth = max(max_depth, depth)

        for child in node.children:
            stack.append((child, depth + 1))

    return max_depth


def test():
    n1 = NaryNode(1)
    n2 = NaryNode(1)
    n3 = NaryNode(1)
    n4 = NaryNode(1)
    n5 = NaryNode(1)
    n6 = NaryNode(1)
    n7 = NaryNode(1)
    n8 = NaryNode(1)
    n9 = NaryNode(1)

    n1.children = [n2, n3]
    n2.children = [n4]
    n4.children = [n5]
    n5.children = [n6]
    n3.children = [n7, n8]
    n7.children = [n9]

    assert max_depth_rec(n1) == 5
    assert max_depth_iter(n1) == 5