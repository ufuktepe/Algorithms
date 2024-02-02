from node import get_linked_list


# Time: O(n)  Space: O(1)
def swap(head, k):
    second = None
    first = None
    cur = head
    i = 0

    while cur:
        i += 1

        if i == k:
            first = cur
            second = head
        elif i > k:
            second = second.next

        cur = cur.next
    first.val, second.val = second.val, first.val

    return head


def test():
    head = get_linked_list(10)
    swap(head, 2)
    nums = [1, 9, 3, 4, 5, 6, 7, 8, 2, 10]

    cur = head
    for num in nums:
        assert cur.val == num
        cur = cur.next


def test_2():
    head = get_linked_list(3)
    swap(head, 1)
    nums = [3, 2, 1]

    cur = head
    for num in nums:
        assert cur.val == num
        cur = cur.next