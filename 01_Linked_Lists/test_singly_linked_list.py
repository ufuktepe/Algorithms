from singly_linked_list import SinglyLinkedList


linked_list = SinglyLinkedList()
linked_list.add_first(2)
linked_list.add_first(5)
linked_list.add_first(1)
linked_list.add_last(3)

linked_list.remove_first()

print(linked_list)