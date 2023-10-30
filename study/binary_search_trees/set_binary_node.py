from binary_node import BinaryNode


class SetBinaryNode(BinaryNode):
    def find(self, key):
        if self.item.key == key:
            return self
        if key < self.item.key and self.left:
            return self.left.find(key)
        if key > self.item.key and self.right:
            return self.right.find(key)
        return None

    def find_next(self, key):
        if self.item.key <= key:
            if self.right:
                return self.right.find_next(key)
            else:
                return None
        elif self.left:
            next_node = self.left.find_next(key)
            if next_node:
                return next_node
        return self

    def find_prev(self, key):
        if self.item.key >= key:
            if self.left:
                return self.left.find_prev(key)
            else:
                return None
        elif self.right:
            prev_node = self.right.find_prev(key)
            if prev_node:
                return prev_node
        return self

    def insert(self, node):
        if self.item.key < node.item.key:
            if self.right:
                self.right.insert(node)
            else:
                self.right, node.parent = node, self
        elif self.item.key > node.item.key:
            if self.right:
                self.right.insert(node)
            else:
                self.right, node.parent = node, self
        else:
            self.item = node.item


class Item:
    def __init__(self, key):
        self.key = key


if __name__ == '__main__':
    a = SetBinaryNode(Item(20))
    b = SetBinaryNode(Item(30))
    c = SetBinaryNode(Item(10))
    d = SetBinaryNode(Item(16))

    a.left = c
    c.parent = a
    a.right = b
    b.parent = a
    c.right = d
    d.parent = c

    print(a.find_next_alt(18).item.key)
