# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from node import Node, get_balanced_bst, get_inorder_vals


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        vals = []

        def traverse(node):
            if node is None:
                vals.append('n')
                return

            vals.append(str(node.val))
            traverse(node.left)
            traverse(node.right)

        traverse(root)
        return ','.join(vals)

    def deserialize(self, data):
        vals = data.split(',')

        def _deserialize(i):
            if i >= len(vals) or vals[i] == 'n':
                return None, i

            node = Node(int(vals[i]))
            node.left, i = _deserialize(i + 1)
            node.right, i = _deserialize(i + 1)

            return node, i

        root, _ = _deserialize(0)
        return root

    def deserialize_iter(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        stack = []
        vals = data.split(',')
        i = 0
        root = None

        while i < len(vals):
            while i < len(vals) and vals[i] == 'n':
                stack.pop()
                i += 1

            if i >= len(vals):
                break

            node = Node(int(vals[i]))
            if root is None:
                root = node

            if stack:
                stack[-1].right = node
                stack.pop()
            stack.append(node)
            i += 1

            while i < len(vals) and vals[i] != 'n':
                node = Node(int(vals[i]))
                stack[-1].left = node
                stack.append(node)
                i += 1

            i += 1

        return root


    def deserialize_iter_v2(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        vals = data.split(',')
        root = Node(int(vals[0]))
        stack = [root]
        i = 1

        while i < len(vals):
            while i < len(vals):
                if vals[i] == 'n':
                    break
                node = Node(int(vals[i]))
                stack[-1].left = node
                stack.append(node)
                i += 1

            i += 1

            while i < len(vals):
                if vals[i] == 'n':
                    stack.pop()
                    i += 1
                else:
                    break
            else:
                break

            node = Node(int(vals[i]))

            if stack:
                stack[-1].right = node
                stack.pop()

            stack.append(node)
            i += 1

        return root


def test():
    root = get_balanced_bst(7)
    codec = Codec()
    s = codec.serialize(root)
    assert s == '4,2,1,n,n,3,n,n,6,5,n,n,7,n,n'
    d = codec.deserialize_r(s)
    inorder = [1, 2, 3, 4, 5, 6, 7]
    assert get_inorder_vals(d) == inorder


def test_2():
    n1 = Node(1)
    n3 = Node(3)
    n2 = Node(2, n1, n3)
    n4 = Node(4, None, n2)
    n8 = Node(8)
    n6 = Node(6, n4, n8)

    codec = Codec()
    s = codec.serialize(n6)
    assert s == '6,4,n,2,1,n,n,3,n,n,8,n,n'
    d = codec.deserialize(s)
    inorder = [4, 1, 2, 3, 6, 8]
    assert get_inorder_vals(d) == inorder