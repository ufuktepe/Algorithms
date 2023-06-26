class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BST:
    def __init__(self, vals):
        self.root = self.generate(vals)

    def generate(self, vals):
        if not vals:
            return None

        mid_idx = len(vals) // 2
        mid_val = vals[mid_idx]
        mid_node = Node(val=mid_val)

        left_tree_root = self.generate(vals[:mid_idx])
        right_tree_root = self.generate(vals[mid_idx+1:])

        if left_tree_root:
            mid_node.left = left_tree_root
        if right_tree_root:
            mid_node.right = right_tree_root

        return mid_node

    def find(self, val):
        return self.search(val, self.root)

    def search(self, val, node):
        if node is None:
            return None

        if node.val == val:
            return node
        elif node.val > val:
            return self.search(val, node.left)
        else:
            return self.search(val, node.right)

def print_values(node):
    if node is None:
        return

    left = 'None' if node.left is None else node.left.val
    right = 'None' if node.right is None else node.right.val

    print(f'Node: {node.val} - Left: {left} - Right: {right}')
    print_values(node.left)
    print_values(node.right)


vals = [1, 2, 3, 4, 5, 6, 7]

bst = BST(vals)

n = bst.find(9)
if n:
    print(n.val)
else:
    print('does not exist.')

# root = bst.root
# print_values(root)

