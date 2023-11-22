def reverse_list_rec(head):
    if head is None:
        return None

    def reverse(node):
        if node.next is None:
            return node, node
        cur_tail, new_head = reverse(node.next)

        cur_tail.next = node
        node.next = None

        return node, new_head

    _, head = reverse(head)

    return head


def reverse_list_iter(head):
    if not head:
        return
    cur = head
    prev = None

    while cur:
        next_cur = cur.next
        cur.next = prev
        prev = cur
        cur = next_cur

    return prev