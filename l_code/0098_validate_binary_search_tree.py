from node import Node


# Time: O(N)  Space: O(N)
def is_valid_bst(root):
    inorder = []

    # O(N)
    def populate_inorder(node):
        if node is None:
            return

        populate_inorder(node.left)
        inorder.append(node.val)
        populate_inorder(node.right)

    populate_inorder(root)

    # O(N)
    for i in range(len(inorder) - 1):
        if inorder[i] >= inorder[i + 1]:
            return False
    return True


def is_valid_bst_v2(root):
    def evaluate(node):
        left_min = right_max = node.val
        left_is_valid = right_is_valid = is_valid = True
        if node.left:
            left_max, left_min, left_is_valid = evaluate(node.left)
            if left_max >= node.val:
                is_valid = False

        if node.right:
            right_max, right_min, right_is_valid = evaluate(node.right)
            if right_min <= node.val:
                is_valid = False

        return right_max, left_min, is_valid and left_is_valid and right_is_valid

    maximum, minimum, is_valid = evaluate(root)
    return is_valid


def is_valid_bst_v3(root):
    def evaluate(node, low=float('-inf'), high=float('inf')):
        if node is None:
            return True

        if not (low < node.val < high):
            return False

        if not evaluate(node.left, low, node.val):
            return False
        if not evaluate(node.right, node.val, high):
            return False

        return True

    return evaluate(root)


def test():
    n1 = Node(1)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n6 = Node(6)

    n5.left, n5.right = n1, n4
    n4.left, n4.right = n3, n6

    assert is_valid_bst_v3(n5) == False