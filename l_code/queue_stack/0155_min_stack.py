class MinStack:

    def __init__(self):
        self.items = []

    def push(self, val: int) -> None:
        """ Pushes the element val onto the stack. """
        curr_min = float('inf') if len(self.items) == 0 else self.getMin()
        new_min = min(curr_min, val)
        self.items.append((val, new_min))

    def pop(self) -> None:
        """ Removes the element on the top of the stack. """
        self.items.pop()

    def top(self):
        """ Gets the top element of the stack. """
        return self.items[-1][0]

    def getMin(self):
        """ Retrieves the minimum element in the stack. """
        return self.items[-1][1]
