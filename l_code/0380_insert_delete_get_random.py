import random


class RandomizedSet(object):
    def __init__(self):
        self.items = []
        self.pos = {}

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.pos:
            self.items.append(val)
            self.pos[val] = len(self.items) - 1
            return True
        return False

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.pos:
            idx = self.pos[val]
            last = self.items[-1]
            self.items[idx] = last
            self.pos[last] = idx
            self.items.pop()
            del self.pos[val]
            return True

        return False

    def getRandom(self):
        """
        :rtype: int
        """
        rand_index = random.randint(0, len(self.items) - 1)
        return self.items[rand_index]


def test_successful_insert():
    rs = RandomizedSet()
    assert rs.insert(5) == True


def test_failed_insert():
    rs = RandomizedSet()
    rs.insert(5)
    assert rs.insert(5) == False


def test_successful_remove():
    rs = RandomizedSet()
    rs.insert(0)
    assert rs.remove(0) == True


def test_failed_remove():
    rs = RandomizedSet()
    assert rs.remove(0) == False