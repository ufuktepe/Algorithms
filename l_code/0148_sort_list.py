import heapq
from node import SLLNode


# Time: O(n*log(n))  Space: O(n)
def sort_list(head):
    heap = []

    cur = head
    while cur:
        heap.append((cur.val, cur))
        cur = cur.next

    heapq.heapify(heap)

    dummy = SLLNode(0)
    cur = dummy
    while heap:
        val, node = heapq.heappop(heap)
        cur.next = node
        cur = cur.next

    return dummy.next


def test():
    n3 = SLLNode(3)
    n1 = SLLNode(1, n3)
    n2 = SLLNode(2, n1)
    n4 = SLLNode(4, n2)

    head = sort_list(n4)
    nums = [1, 2, 3, 4]
    cur = head
    for num in nums:
        assert num == cur.val
        cur = cur.next