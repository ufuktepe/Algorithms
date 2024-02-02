from node import get_linked_list


# Time: O(n)  Space: O(1)
def reverse_k_group(head, k):
    def reverse_list(head, k):
        cur = head
        prev = None

        while k > 0:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node
            k -= 1

        return prev, cur

    def has_enough_nodes(node, k):
        cur = node

        while k > 0:
            if cur is None:
                return False

            cur = cur.next
            k -= 1

        return True

    cur = head
    last_tail = None
    new_head = None

    while has_enough_nodes(cur, k):
        local_head, next_head = reverse_list(cur, k)
        if new_head is None:
            new_head = local_head
        if last_tail:
            last_tail.next = local_head

        last_tail = cur
        cur.next = next_head
        cur = next_head

    return new_head if new_head is not None else head


def test():
    head = get_linked_list(4)
    new_head = reverse_k_group(head, k=2)
    res = [2, 1, 4, 3]

    cur = new_head
    for num in res:
        assert num == cur.val
        cur = cur.next


def test_2():
    head = get_linked_list(5)
    new_head = reverse_k_group(head, k=2)
    res = [2, 1, 4, 3, 5]

    cur = new_head
    for num in res:
        assert num == cur.val
        cur = cur.next


def test_3():
    head = get_linked_list(8)
    new_head = reverse_k_group(head, k=3)
    res = [3, 2, 1, 6, 5, 4, 7, 8]

    cur = new_head
    for num in res:
        assert num == cur.val
        cur = cur.next