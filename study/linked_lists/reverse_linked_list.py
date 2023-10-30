class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def reverse_linked_list(head):
    """Iteratively replace the head node."""
    cur = head.next
    head.next = None

    while cur:
        next_cur = cur.next
        cur.next = head
        head = cur
        cur = next_cur

    return head


def reverse_linked_list_recursive(node, prev=None):
    """Recursive solution."""
    if not node:
        return prev
    next_node = node.next
    node.next = prev

    return reverse_linked_list_recursive(next_node, prev=node)


def iterative(head):
    """Simple iterative solution."""
    cur = head.next
    head.next = None
    prev = head

    while cur:
        next_node = cur.next
        cur.next = prev
        prev = cur
        cur = next_node

    return prev


def recursive(node, prev=None):
    if not node:
        return prev

    next_node = node.next
    node.next = prev
    return recursive(next_node, node)


if __name__ == '__main__':
    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    e = Node('e')

    head = a
    a.next = b
    b.next = c
    c.next = d
    d.next = e

    head = recursive(head)

    cur = head
    while cur:
        print(cur.val)
        cur = cur.next






















