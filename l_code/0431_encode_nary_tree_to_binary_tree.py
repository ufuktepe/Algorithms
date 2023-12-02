from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



class Codec:
    # Encodes an n-ary tree to a binary tree.
    def encode(self, root: 'Optional[Node]') -> Optional[TreeNode]:
        if root is None:
            return root

        def build_tree(node, tree_node, siblings):
            if node.children:
                tree_node.left = TreeNode(node.children[0].val)
                build_tree(node.children[0], tree_node.left, node.children[1:])

            if siblings:
                tree_node.right = TreeNode(siblings[0].val)
                build_tree(siblings[0], tree_node.right, siblings[1:])

        root_tree_node = TreeNode(root.val)
        build_tree(root, root_tree_node, [])

        return root_tree_node

    # Decodes your binary tree to an n-ary tree.
    def decode(self, data: Optional[TreeNode]) -> 'Optional[Node]':
        if data is None:
            return data

        root_node = Node(data.val)
        stack = [(data, root_node)]

        while stack:
            tree_node, node = stack.pop()

            children = []
            if tree_node.left:
                child_node = Node(tree_node.left.val)
                children.append(child_node)
                stack.append((tree_node.left, child_node))

                cur_tree_node = tree_node.left.right

                while cur_tree_node:
                    child_node = Node(cur_tree_node.val)
                    children.append(child_node)
                    stack.append((cur_tree_node, child_node))
                    cur_tree_node = cur_tree_node.right

            node.children = children

        return root_node

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(root))