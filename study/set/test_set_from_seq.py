from study.set.set_from_seq import SetFromSeq
from study.linked_lists.singly_linked_list import SinglyLinkedList


class Item:
    def __init__(self, key):
        self.key = key


def test_find():
    a = SetFromSeq(SinglyLinkedList)
    a.build([Item(3), Item(1), Item(5)])
    item = a.find(3)
    assert item.key == 3


def test_insert():
    a = SetFromSeq(SinglyLinkedList)
    a.build([Item(3), Item(1), Item(5)])
    a.insert(Item(4))
    item = a.find(4)
    assert item.key == 4


def test_delete():
    a = SetFromSeq(SinglyLinkedList)
    a.build([Item(3), Item(1), Item(5)])
    item_1 = a.delete(Item(3))
    assert item_1.key == 3
    item_2 = a.find(3)
    assert item_2 is None


def test_find_min():
    a = SetFromSeq(SinglyLinkedList)
    a.build([Item(3), Item(1), Item(5)])
    item = a.find_min()
    assert item.key == 1


def test_find_max():
    a = SetFromSeq(SinglyLinkedList)
    a.build([Item(3), Item(1), Item(5)])
    item = a.find_max()
    assert item.key == 5


def test_find_next():
    a = SetFromSeq(SinglyLinkedList)
    a.build([Item(3), Item(1), Item(5)])
    item = a.find_next(3)
    assert item.key == 5


def test_find_prev():
    a = SetFromSeq(SinglyLinkedList)
    a.build([Item(3), Item(1), Item(5)])
    item = a.find_prev(3)
    assert item.key == 1
