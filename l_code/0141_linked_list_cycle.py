from node import get_linked_list


# Time O(n)  Space: O(1)
def has_cycle(head):
    if not head:
        return False

    slow = fast = head
    
    while slow.next and fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

        if slow is fast:
            return True

    return False


def test():
    head = get_linked_list(1)
    assert has_cycle(head) is False


def test_2():
    head = get_linked_list(2)
    assert has_cycle(head) is False


def test_3():
    head = get_linked_list(5)
    assert has_cycle(head) is False


def test_4():
    head = get_linked_list(2)
    tail = head.next
    tail.next = head
    assert has_cycle(head)


def test_5():
    head = get_linked_list(5)
    cur = head
    while cur.next:
        cur = cur.next

    cur.next = head.next

    assert has_cycle(head)


def test_6():
    head = get_linked_list(5)
    cur = head
    while cur.next:
        cur = cur.next

    cur.next = head.next.next

    assert has_cycle(head)