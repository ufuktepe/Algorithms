import pytest
from array_seq import ArraySeq


def test_set_at_and_get_at():
    a = ArraySeq()
    a.build([None, None, None])
    a.set_at(1, 1)
    assert a.get_at(1) == 1
    assert len(a) == 3


def test_invalid_set_at():
    a = ArraySeq()
    a.build([None, None, None])
    with pytest.raises(IndexError):
        a.set_at(3, 1)


def test_invalid_get_at():
    a = ArraySeq()
    with pytest.raises(IndexError):
        a.get_at(0)


def test_insert_at():
    a = ArraySeq()
    a.build([1, 2, 3])
    a.insert_at(0, 10)
    assert a.get_at(0) == 10
    assert len(a) == 4


def test_invalid_insert_at():
    a = ArraySeq()
    a.build([1, 2, 3])
    with pytest.raises(IndexError):
        a.insert_at(10, 10)


def test_delete_at():
    a = ArraySeq()
    a.build([1, 2, 3])
    a.delete_at(1)
    assert a.get_at(0) == 1
    assert a.get_at(1) == 3
    assert len(a) == 2


def test_invalid_delete_at():
    a = ArraySeq()
    a.build([1, 2, 3])
    with pytest.raises(IndexError):
        a.delete_at(3)


def test_insert_first():
    a = ArraySeq()
    a.insert_first(10)
    assert a.get_at(0) == 10
    assert len(a) == 1


def test_delete_first():
    a = ArraySeq()
    a.build([1, 2, 3])
    a.delete_first()
    assert a.get_at(0) == 2
    assert a.get_at(1) == 3
    assert len(a) == 2


def test_invalid_delete_first():
    a = ArraySeq()
    with pytest.raises(IndexError):
        a.delete_first()


def test_insert_last():
    a = ArraySeq()
    a.insert_last(10)
    assert a.get_at(0) == 10
    assert len(a) == 1


def test_delete_last():
    a = ArraySeq()
    a.build([1, 2, 3])
    a.delete_last()
    assert a.get_at(0) == 1
    assert a.get_at(1) == 2
    assert len(a) == 2


def test_invalid_delete_last():
    a = ArraySeq()
    with pytest.raises(IndexError):
        a.delete_last()