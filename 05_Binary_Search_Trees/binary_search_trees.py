class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BST:git
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

    def insert(self, val):
        curr_node = self.root

        while True:
            if val < curr_node.val:
                if curr_node.left:
                    curr_node = curr_node.left
                else:
                    curr_node.left = Node(val)
                    break

            elif curr_node.right:
                curr_node = curr_node.right
            else:
                curr_node.right = Node(val)
                break


def delete(val, node):
    if node is None:
        return None

    if val < node.val:
        node.left = delete(val, node.left)
        return node

    elif val > node.val:
        node.right = delete(val, node.right)
        return node

    else:
        # Need to delete the current node
        # If there is no left child, return the right child
        if node.left is None:
            return node.right

        # If there is no right child, return the left child
        if node.right is None:
            return node.left

        # If it has two children, find the successor
        node.right = lift(node.right, node)
        return node


def lift(node, node_to_delete):
    if node.left is not None:
        node.left = lift(node.left, node_to_delete)
        return node
    else:
        node_to_delete.val = node.val
        return node.right


def insert_recursive(val, root):
    if val < root.val:
        if root.left:
            insert_recursive(val, root.left)
        else:
            root.left = Node(val)

    elif root.right:
        insert_recursive(val, root.right)

    else:
        root.right = Node(val)


def print_values(node):
    if node is None:
        return

    left = 'None' if node.left is None else node.left.val
    right = 'None' if node.right is None else node.right.val

    print_values(node.left)
    print(f'Node: {node.val} - Left: {left} - Right: {right}')
    print_values(node.right)


vals = [1, 2, 3, 4, 5, 6, 7]

bst = BST(vals)

delete(4, bst.root)

print_values(bst.root)

# n = bst.find(9)
# if n:
#     print(n.val)
# else:
#     print('does not exist.')

# root = bst.root
# print_values(root)

