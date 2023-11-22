from node import SLLNode


# Time: O(N)  Space: O(N) due to recursive stack
def swap_pairs(head):
    if head and head.next:
        next_node = head.next.next
        new_head = head.next
        new_head.next = head
        head.next = swap_pairs(next_node)

        return new_head
    return head


def test():
    d = SLLNode(4)
    c = SLLNode(3, next=d)
    b = SLLNode(2, next=c)
    a = SLLNode(1, next=b)

    swap_pairs(a)

    assert a.next == d
    assert b.next == a
    assert c.next is None
    assert d.next == c