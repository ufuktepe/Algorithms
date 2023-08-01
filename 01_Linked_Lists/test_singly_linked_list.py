import pytest

from singly_linked_list import SinglyLinkedList


def test_set_at_and_get_at():
    sll = SinglyLinkedList()
    sll.build([1, 2, 3, 4, 5])
    sll.set_at(1, 10)
    assert sll.get_at(1) == 10
    assert len(sll) == 5


def test_invalid_set_at():
    sll = SinglyLinkedList()
    sll.build([1, 2, 3, 4, 5])
    with pytest.raises(IndexError):
        sll.set_at(5, 10)


def test_invalid_get_at():
    sll = SinglyLinkedList()
    sll.build([1, 2, 3, 4, 5])
    with pytest.raises(IndexError):
        sll.get_at(5)


def test_insert_first():
    sll = SinglyLinkedList()
    sll.insert_first(7)
    assert sll.get_at(0) == 7
    assert len(sll) == 1


def test_delete_first():
    sll = SinglyLinkedList()
    sll.build([1, 2, 3, 4, 5])
    sll.delete_first()
    assert sll.get_at(0) == 2
    assert sll.get_at(3) == 5
    assert len(sll) == 4


def test_insert_at():
    sll = SinglyLinkedList()
    sll.build([1, 2, 3, 4, 5])
    sll.insert_at(1, 10)
    assert sll.get_at(0) == 1
    assert sll.get_at(1) == 10
    assert sll.get_at(2) == 2
    assert len(sll) == 6


def test_invalid_insert_at():
    sll = SinglyLinkedList()
    sll.build([1, 2, 3, 4, 5])
    with pytest.raises(IndexError):
        sll.insert_at(6, 10)


def test_delete_at():
    sll = SinglyLinkedList()
    sll.build([1, 2, 3, 4, 5])
    sll.delete_at(4)
    assert sll.get_at(0) == 1
    assert sll.get_at(3) == 4
    assert len(sll) == 4


def test_invalid_delete_at():
    sll = SinglyLinkedList()
    sll.build([1, 2, 3, 4, 5])
    with pytest.raises(IndexError):
        sll.delete_at(5)


def test_insert_last():
    sll = SinglyLinkedList()
    sll.build([1, 2, 3, 4, 5])
    sll.insert_last(6)
    assert sll.get_at(0) == 1
    assert sll.get_at(5) == 6
    assert len(sll) == 6


def test_delete_last():
    sll = SinglyLinkedList()
    sll.build([1, 2, 3, 4, 5])
    sll.delete_last()
    assert sll.get_at(0) == 1
    assert sll.get_at(3) == 4
    assert len(sll) == 4


def test_invalid_delete_last():
    sll = SinglyLinkedList()
    with pytest.raises(IndexError):
        sll.delete_last()