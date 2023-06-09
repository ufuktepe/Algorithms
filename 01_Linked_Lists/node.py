class Node:
    def __init__(self, val):
        self.val = val
        self._next = None
        self._previous = None

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, next_node):
        self._next = next_node

    @property
    def previous(self):
        return self._previous

    @previous.setter
    def previous(self, previous_node):
        self._previous = previous_node
