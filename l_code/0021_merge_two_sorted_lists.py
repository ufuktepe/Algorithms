from node import SLLNode


# Time: O(N+M)  Space: O(1)
def merge_two_lists_iter(list1, list2):
    if list1 is None:
        return list2
    if list2 is None:
        return list1

    if list1.val < list2.val:
        head = list1
        list1 = list1.next
    else:
        head = list2
        list2 = list2.next

    cur = head
    while list1 and list2:
        if list1.val < list2.val:
            cur.next = list1
            list1 = list1.next
        else:
            cur.next = list2
            list2 = list2.next
        cur = cur.next

    if list1:
        cur.next = list1
    if list2:
        cur.next = list2

    return head


# Time: O(N+M)  Space: O(N+M) because stack frames consume O(N+M) space
def merge_two_lists_rec(list1, list2):
    if list1 is None:
        return list2
    if list2 is None:
        return list1

    if list1.val < list2.val:
        list1.next = merge_two_lists_rec(list1.next, list2)
        return list1
    else:
        list2.next = merge_two_lists_rec(list1, list2.next)
        return list2


def test_iter():
    c1 = SLLNode(10)
    b1 = SLLNode(5, next=c1)
    a1 = SLLNode(1, next=b1)

    c2 = SLLNode(12)
    b2 = SLLNode(4, next=c2)
    a2 = SLLNode(2, next=b2)

    cur = merge_two_lists_iter(a1, a2)

    sorted_list = [a1, a2, b2, b1, c1, c2]

    for n in sorted_list:
        assert cur == n
        cur = cur.next


def test_rec():
    c1 = SLLNode(10)
    b1 = SLLNode(5, next=c1)
    a1 = SLLNode(1, next=b1)

    c2 = SLLNode(12)
    b2 = SLLNode(4, next=c2)
    a2 = SLLNode(2, next=b2)

    cur = merge_two_lists_rec(a1, a2)

    sorted_list = [a1, a2, b2, b1, c1, c2]

    for n in sorted_list:
        assert cur == n
        cur = cur.next
