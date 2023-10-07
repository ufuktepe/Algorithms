class DoublyLinkedList:

    class Node:
        def __init__(self, val, next=None, prev=None):
            self.val = val
            self.next = next
            self.prev = prev

    def __init__(self):
        self.head = self.Node(val='head')
        self.tail = self.Node(val='tail')
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def __len__(self):
        return self.size

    def insert_between(self, val, predecessor, successor):
        node = self.Node(val)
        predecessor.next = node
        node.prev = predecessor

        successor.prev = node
        node.next = successor

        self.size += 1

        return node

    def delete_node(self, node):
        predecessor = node.prev
        successor = node.next

        if not (predecessor and successor):
            return

        predecessor.next = successor
        successor.prev = predecessor

        self.size -= 1

        val = node.item
        node.prev = node.next = node.item = None  # deprecate node

        return val
