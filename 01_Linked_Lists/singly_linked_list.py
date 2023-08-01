from singly_linked_list_node import SinglyLinkedListNode as Node


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self):
        return self.size

    def __iter__(self):
        curr_node = self.head
        while curr_node:
            yield curr_node.val
            curr_node = curr_node.next

    def build(self, vals):
        for item in reversed(vals):
            self.insert_first(item)

    def _get_node_at(self, i):
        if not (0 <= i < self.size):
            raise IndexError
        curr_node = self.head
        while i > 0:
            curr_node = curr_node.next
            i -= 1

        return curr_node

    def get_at(self, i):
        node = self._get_node_at(i)
        return node.val

    def set_at(self, i, val):
        node = self._get_node_at(i)
        node.val = val

    def insert_first(self, val):
        new_node = Node(val, next=self.head)
        self.head = new_node
        self.size += 1

    def delete_first(self):
        if self.head is None:
            return
        val = self.head.val
        self.head = self.head.next
        self.size -= 1

        return val

    def insert_at(self, i, val):
        if i == 0:
            self.insert_first(val)
            return

        new_node = Node(val)
        prev_node = self._get_node_at(i - 1)
        new_node.next = prev_node.next
        prev_node.next = new_node
        self.size += 1

    def delete_at(self, i):
        if i == 0:
            return self.delete_first()

        prev_node = self._get_node_at(i - 1)
        node = self._get_node_at(i)
        val = node.val
        prev_node.next = node.next
        self.size -= 1

        return val

    def insert_last(self, val):
        self.insert_at(self.size, val)

    def delete_last(self):
        self.delete_at(self.size - 1)

    # def add_first(self, val):
    #     node = self.Node(val, next=self.head)
    #     self.head = node
    #
    #     if self.tail is None:
    #         self.tail = node
    #
    #     self.size += 1
    #
    # def remove_first(self):
    #     if self.head is None:
    #         return
    #     self.head = self.head.next
    #     self.size -= 1
    #
    # def add_last(self, val):
    #     node = self.Node(val)
    #     self.tail.next = node
    #     self.tail = node
    #     self.size += 1

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


ssl = SinglyLinkedList()
a = [1, 3, 5, 7, 23, 2]
ssl.build(a)

for item in ssl:
    print(item)