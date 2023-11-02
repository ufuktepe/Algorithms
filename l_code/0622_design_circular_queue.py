class MyCircularQueue(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.items = [None] * k
        self.head = 0  # Index of first item
        self.tail = 0  # Next index of last item (index of available spot)

    def _incr(self, x):
        return (x + 1) % len(self.items)

    def _decr(self, x):
        return (x - 1) % len(self.items)

    def enQueue(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if not self.isFull():
            self.items[self.tail] = value
            self.tail = self._incr(self.tail)
            return True

    def deQueue(self):
        """
        :rtype: bool
        """
        if not self.isEmpty():
            self.items[self.head] = None
            self.head = self._incr(self.head)
            return True

    def Front(self):
        """
        :rtype: int
        """
        if self.isEmpty():
            return -1

        return self.items[self.head]

    def Rear(self):
        """
        :rtype: int
        """
        if self.isEmpty():
            return -1

        idx = self._decr(self.tail)
        return self.items[idx]

    def isEmpty(self):
        """
        :rtype: bool
        """
        return (self.head == self.tail) and (self.items[self.head] is None)

    def isFull(self):
        """
        :rtype: bool
        """
        return (self.head == self.tail) and (self.items[self.head] is not None)


def test_my_circular_queue():
    cq = MyCircularQueue(3)
    assert cq.enQueue(1) == True
    assert cq.enQueue(2) == True
    assert cq.enQueue(3) == True
    cq.enQueue(4)
    assert cq.Front() == 1
    assert cq.deQueue() == True
    assert cq.Rear() == 2
