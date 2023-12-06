from node import get_balanced_bst, Node


# Time: O(N)  Space: O(H)
def bst_to_dll(root):
    if root is None:
        return root

    head = None
    prev = None

    def traverse(node):
        if node is None:
            return

        nonlocal prev
        nonlocal head

        traverse(node.left)

        if head is None:
            head = node
        else:
            prev.right = node
            node.left = prev
        prev = node

        traverse(node.right)

    traverse(root)

    head.left = prev
    prev.right = head

    return head


# Time: O(N)  Space: O(H)
def bst_to_dll_divide_and_conquer(root):
    if root is None:
        return None

    def get_head_tail(node):
        if node is None:
            return None, None

        left_head, left_tail = get_head_tail(node.left)
        right_head, right_tail = get_head_tail(node.right)

        node.left = left_tail
        node.right = right_head

        if left_tail is not None:
            left_tail.right = node

        if right_head is not None:
            right_head.left = node

        head = node if left_head is None else left_head
        tail = node if right_tail is None else right_tail

        return head, tail

    head, tail = get_head_tail(root)

    head.left = tail
    tail.right = head

    return head


# Time: O(N)  Space: O(H)
def bst_to_dll_iter(root):
    if root is None:
        return None

    stack = []
    cur = root
    head = prev = None

    while stack or cur:
        while cur:
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()
        if head:
            cur.left = prev
            prev.right = cur
        else:
            head = cur
        prev = cur
        cur = cur.right

    head.left = prev
    prev.right = head

    return head


def test():
    root = get_balanced_bst(7)
    head = bst_to_dll_iter(root)

    for _ in range(6):
        assert head.right.val - head.val == 1
        assert head.right.left.val == head.val


def test_bst_with_one_node():
    root = Node(1)
    head = bst_to_dll_iter(root)

    assert head.left is head
    assert head.right is head