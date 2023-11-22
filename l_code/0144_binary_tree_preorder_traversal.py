# Definition for a binary tree node.
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def preorderTraversal_recursive(root):
    res = []

    def traverse(root):
        if root is None:
            return

        res.append(root.val)
        traverse(root.left)
        traverse(root.right)

    traverse(root)
    return res

# Time: O(n)  Space: O(n)
def preorderTraversal_iterative(root):
    res = []
    if root is None:
        return res
    stack = [root]

    while stack:
        cur = stack.pop()
        res.append(cur.val)

        if cur.right:
            stack.append(cur.right)
        if cur.left:
            stack.append(cur.left)

    return res




def test_1():
    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    e = Node('e')

    b.left = d
    c.right = e
    a.left, a.right = b, c
    assert preorderTraversal_iterative(a) == ['a', 'b', 'd', 'c', 'e']
    assert preorderTraversal_iterative(None) == []
    assert preorderTraversal_iterative(e) == ['e']