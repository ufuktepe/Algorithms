from doubly_linked_list import DoublyLinkedList

def test_empty_dll():
    dll = DoublyLinkedList()
    assert dll.is_empty()

def test_non_empty_dll():
    dll = DoublyLinkedList()
    dll.insert_between(5, dll.head, dll.tail)
    assert dll.is_empty() is False

def test_delete_node():
    dll = DoublyLinkedList()
    node = dll.insert_between(5, dll.head, dll.tail)
    dll.delete_node(node)
    assert dll.is_empty() is True