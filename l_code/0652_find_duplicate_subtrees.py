# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_duplicate_subtrees(root):
    """
    :type root: TreeNode
    :rtype: List[TreeNode]
    """
    hmap = {}
    res = []

    def populate_hmap(node):
        if node is None:
            return '.'

        tree = ''.join([populate_hmap(node.left), str(node.val), populate_hmap(node.right)])

        if tree in hmap:
            hmap[tree] += 1
            if hmap[tree] == 2:
                res.append(node)
        else:
            hmap[tree] = 1

        return tree

    populate_hmap(root)
    return res


d = TreeNode(val=4)
f = TreeNode(val=4)
g = TreeNode(val=4)
e = TreeNode(val=2, left=g)
c = TreeNode(val=3, left=e, right=f)
b = TreeNode(val=2, left=d)
a = TreeNode(val=1, left=b, right=c)

res = find_duplicate_subtrees(a)

for n in res:
    print(n.val)
