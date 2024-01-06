from node import SLLNode

# Let n be the number of nodes in the linked list
# Time: O(n)  Space: O(1)
def delete_node(node):
    cur = node
    prev = None

    while cur.next:
        prev = cur
        cur.val = cur.next.val
        cur = cur.next

    prev.next = None


def test():
    n5 = SLLNode(5)
    n4 = SLLNode(4, n5)
    n3 = SLLNode(3, n4)
    n2 = SLLNode(2, n3)
    n1 = SLLNode(1, n2)

    delete_node(n3)

    assert n1.val == 1
    assert n1.next.val == 2
    assert n2.next.val == 4
    assert n3.next.val == 5
    assert n4.next is None
