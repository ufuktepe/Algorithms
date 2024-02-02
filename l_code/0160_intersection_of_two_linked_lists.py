from node import get_linked_list


# Time: O(m + n)  Space: O(1)  where m is length of headA and n is length of headB
def get_intersection_node(headA, headB):
    cur_a = headA
    cur_b = headB

    while True:
        if cur_a is cur_b:
            return cur_a

        cur_a = cur_a.next
        cur_b = cur_b.next

        if not cur_a and not cur_b:
            break

        if not cur_a:
            cur_a = headB

        if not cur_b:
            cur_b = headA

    return None


def test():
    headA = get_linked_list(3)
    headB = get_linked_list(4)
    assert get_intersection_node(headA, headB) is None


def test_2():
    headA = get_linked_list(3)
    headB = get_linked_list(1)

    headB.next = headA.next.next

    assert get_intersection_node(headA, headB) is headB.next