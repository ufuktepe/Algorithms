class SinglyLinkedList:

    class Node:
        def __init__(self, val, next=None):
            self.val = val
            self.next = next

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add_first(self, val):
        node = self.Node(val, next=self.head)
        self.head = node

        if self.tail is None:
            self.tail = node

        self.size += 1

    def remove_first(self):
        if self.head is None:
            return
        self.head = self.head.next
        self.size -= 1

    def add_last(self, val):
        node = self.Node(val)
        self.tail.next = node
        self.tail = node
        self.size += 1

    def __str__(self):
        str_rep_items = ['[']
        curr_node = self.head
        while curr_node:
            if curr_node != self.head:
                str_rep_items.append(', ')
            str_rep_items.append(str(curr_node.val))

            curr_node = curr_node.next

        str_rep_items.append(']')

        return ''.join(str_rep_items)
