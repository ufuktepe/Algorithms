from node import get_linked_list


# Let k be the number of nodes in the linked list
# Time: O(k)  Space: O(1)
def remove_node(head, n):
    node = head
    prev_node = None
    cur = head
    k = 0

    while cur:
        k += 1
        if k > n:
            prev_node = node
            node = node.next
        cur = cur.next

    if prev_node:
        prev_node.next = node.next
        return head

    return head.next


def test():
    head = get_linked_list(2)
    new_head = remove_node(head, 2)
    assert new_head.val == 2
    assert new_head.next is None


def test_2():
    head = get_linked_list(4)
    new_head = remove_node(head, 2)
    vals = [1, 2, 4]

    cur = new_head
    for val in vals:
        assert cur.val == val
        cur = cur.next