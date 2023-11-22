from node import Node


# Time: O(N)
def is_symmetric(root):
    def is_identical(root1, root2):
        if root1 is None and root2 is None:
            return True

        if root1 is None or root2 is None or root1.val != root2.val:
            return False

        return is_identical(root1.left, root2.right) and is_identical(root1.right, root2.left)

    if root is None:
        return True

    return is_identical(root.left, root.right)


def is_symmetric_iter(root):
    if root is None or (root.left is None and root.right is None):
        return True
    if root.left is None or root.right is None:
        return False

    stack1, stack2 = [root.left], [root.right]

    while stack1 and stack2:
        node1 = stack1.pop()
        node2 = stack2.pop()

        if node1 is None and node2 is None:
            continue

        if node1 is None or node2 is None:
            return False

        if node1.val != node2.val:
            return False

        stack1.append(node1.left)
        stack1.append(node1.right)

        stack2.append(node2.right)
        stack2.append(node2.left)

    if stack1 or stack2:
        return False

    return True

def test_success():
    a = Node('a')
    b_l = Node('b')
    b_r = Node('b')
    c_l = Node('c')
    c_r = Node('c')
    a.left, a.right = b_l, b_r
    b_l.right = c_l
    b_r.left = c_r

    assert is_symmetric(a) == True
    assert is_symmetric_iter(a) == True