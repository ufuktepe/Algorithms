class MyQueue(object):

    def __init__(self):
        self.stack_1 = []
        self.stack_2 = []

    def _transfer(self):
        if not self.stack_2:
            while self.stack_1:
                self.stack_2.append(self.stack_1.pop())

    def push(self, x):
        """
        Pushes element x to the back of the queue.
        :type x: int
        :rtype: None
        """
        self.stack_1.append(x)

    def pop(self):
        """
        Removes the element from the front of the queue and returns it.
        :rtype: int
        """
        self._transfer()
        return self.stack_2.pop()

    def peek(self):
        """
        Returns the element at the front of the queue.
        :rtype: int
        """
        self._transfer()
        return self.stack_2[-1]

    def empty(self):
        """
        Returns true if the queue is empty, false otherwise.
        :rtype: bool
        """
        return not self.stack_1 and not self.stack_2


def test_my_queue():
    q = MyQueue()
    q.push(1)
    q.push(2)
    assert q.peek() == 1
    assert q.pop() == 1
    assert q.empty() == False