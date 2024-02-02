from node import SLLNode

import heapq
from collections import defaultdict


# Let k be the number of linked lists and n be the max number of items among all linked lists
# Time: O(n*k*log(k))  Space: O(k)
def merge_k_lists(lists):
    heap = []
    nodes = defaultdict(list)

    # O(k)
    for head in lists:
        if head is None:
            continue
        heap.append(head.val)
        nodes[head.val].append(head)

    # O(k)
    heapq.heapify(heap)

    dummy = SLLNode()
    cur = dummy

    # O(n*k*log(k))
    while heap:
        val = heapq.heappop(heap)  # O(log(k))
        node = nodes[val].pop()
        cur.next = node
        cur = cur.next

        if node.next:
            heapq.heappush(heap, node.next.val)
            nodes[node.next.val].append(node.next)  # O(log(k))

    return dummy.next


def get_linked_list(lst):
    dummy = SLLNode()
    cur = dummy
    for val in lst:
        node = SLLNode(val)
        cur.next = node
        cur = cur.next

    return dummy.next


def test():
    lst_1 = get_linked_list([1, 30, 45])
    lst_2 = get_linked_list([30, 32, 33])
    head = merge_k_lists([lst_1, lst_2])

    cur = head
    res = []
    while cur:
        res.append(cur.val)
        cur = cur.next

    assert res == [1, 30, 30, 32, 33, 45]
