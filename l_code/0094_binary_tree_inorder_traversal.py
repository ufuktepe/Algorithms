class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorderTraversal(root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    stack = []
    if root is None:
        return stack

    vals = []

    while stack or root:
        while root:
            stack.append(root)
            root = root.left

        node = stack.pop()
        vals.append(node.val)
        root = node.right

    return vals


def inorderTraversal_iter(root):
    stack = []
    res = []
    cur = root

    while stack or cur:
        if cur:
            stack.append(cur)
            cur = cur.left
        else:
            temp_node = stack.pop()
            res.append(temp_node.val)
            cur = temp_node.right

    return res



def test_1():
    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    e = Node('e')
    f = Node('f')
    g = Node('g')
    h = Node('h')

    d.right = e
    b.left = d
    g.left = h

    c.left, c.right = f, g
    a.left, a.right = b, c

    assert inorderTraversal_iter(a) == ['d', 'e', 'b', 'a', 'f', 'c', 'h', 'g']






















