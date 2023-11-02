from collections import deque


class MyStack(object):

    def __init__(self):
        self.queue = deque([])

    def _rotate(self, n):
        for i in range(n):
            self.push(self.queue.popleft())

    def push(self, x):
        """
        Pushes element x to the top of the stack.
        :type x: int
        :rtype: None
        """
        self.queue.append(x)

    def pop(self):
        """
        Removes the element on the top of the stack and returns it.
        :rtype: int
        """
        self._rotate(len(self.queue) - 1)
        return self.queue.popleft()

    def top(self):
        """
        Returns the element on the top of the stack.
        :rtype: int
        """
        self._rotate(len(self.queue) - 1)
        item = self.queue[0]
        self._rotate(1)
        return item

    def empty(self):
        """
        Returns true if the stack is empty, false otherwise.
        :rtype: bool
        """
        return len(self.queue) == 0


def test_my_stack():
    s = MyStack()
    s.push(1)
    s.push(2)
    assert s.top() == 2
    assert s.pop() == 2
    assert s.empty() == False