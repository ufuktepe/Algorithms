class Node:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node


def is_palindrome(head):
    """
    :type head: Node
    :rtype: bool
    """
    if not head:
        return

    # Find the first node of the second half
    fast = slow = head
    while fast.next and fast.next.next:
        fast = fast.next.next
        slow = slow.next

    first_node = slow.next

    # Reverse the 2nd half
    cur = first_node
    prev = None
    while cur:
        next_node = cur.next
        cur.next = prev
        prev = cur
        cur = next_node

    # Compare the reversed second half nodes to first half nodes
    node_b = prev  # First node of the reversed 2nd half
    node_a = head  # First node of the 1st half
    while node_b:
        if node_a.val != node_b.val:
            return False
        node_b = node_b.next
        node_a = node_a.next

    return True


if __name__ == '__main__':
    c = Node('1')
    b = Node('2', next_node=c)
    a = Node('1', next_node=b)

    print(is_palindrome(a))