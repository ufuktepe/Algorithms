from study.set.sorted_array_set import SortedArraySet


class Item:
    def __init__(self, key):
        self.key = key


def test_find_min():
    a = SortedArraySet()
    a.build([Item(3), Item(1), Item(5)])
    min_item = a.find_min()
    assert min_item.key == 1


def test_find_max():
    a = SortedArraySet()
    a.build([Item(3), Item(1), Item(5)])
    max_item = a.find_max()
    assert max_item.key == 5


def test_find():
    a = SortedArraySet()
    a.build([Item(3), Item(1), Item(5)])
    item_1 = a.find(3)
    assert item_1.key == 3
    item_2 = a.find(2)
    assert item_2 is None


def test_find_next():
    a = SortedArraySet()
    a.build([Item(3), Item(1), Item(5)])
    next_item_1 = a.find_next(3)
    assert next_item_1.key == 5
    next_item_2 = a.find_next(5)
    assert next_item_2 is None


def test_find_prev():
    a = SortedArraySet()
    a.build([Item(3), Item(1), Item(5)])
    prev_item_1 = a.find_prev(3)
    assert prev_item_1.key == 1
    prev_item_2 = a.find_prev(1)
    assert prev_item_2 is None


def test_insert():
    a = SortedArraySet()
    a.build([Item(3), Item(1), Item(5)])
    a.insert(Item(7))
    item = a.find(7)
    assert item.key == 7


def test_delete():
    a = SortedArraySet()
    a.build([Item(3), Item(1), Item(5)])
    a.delete(3)
    item = a.find(3)
    assert item is None