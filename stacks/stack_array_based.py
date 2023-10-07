

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) == 0:
            return None

        item = self.items[-1]
        self.items = self.items[:-1]

        return item

    def top(self):
        if len(self.items) == 0:
            return None
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def __len__(self):
        return len(self.items)
