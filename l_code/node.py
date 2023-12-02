class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class SLLNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class NaryNode:
    def __init__(self, val=0, children=None):
        self.val = val
        self.children = [] if children is None else children


def get_balanced_bst(n):
    if n < 1:
        return None

    def generate_bst(low, high):
        if low > high:
            return None

        mid = (low + high) // 2

        root = Node(mid)
        root.left = generate_bst(low, mid - 1)
        root.right = generate_bst(mid + 1, high)

        return root

    return generate_bst(1, n)


def get_inorder_vals(root):
    inorder = []

    def populate_inorder(node):
        if node is None:
            return
        populate_inorder(node.left)
        inorder.append(node.val)
        populate_inorder(node.right)

    populate_inorder(root)
    return inorder
