from set_binary_node import SetBinaryNode
from binary_tree import BinaryTree


class SetBinaryTree(BinaryTree):
    def __init__(self):
        super().__init__(Node_Type=SetBinaryNode)

    def iter_order(self):
        yield from self

    def find_min(self):
        if self.root:
            return self.root.get_first_node_in_subtree().item
        return None

    def find_max(self):
        if self.root:
            return self.root.get_last_node_in_subtree().item
        return None

    def find(self, key):
        if self.root:
            node = self.root.find(key).item
            if node:
                return node.item

    def find_next(self, key):
        if self.root:
            node = self.root.find_next(key)
            if node:
                return node.item

    def find_prev(self, key):
        if self.root:
            node = self.root.find_prev(key)
            if node:
                return node.item

    def insert(self, item):
        new_node = self.Node_Type(item)
        if self.root:
            self.root.insert(new_node)
        else:
            self.root = new_node
        self.size += 1

    def delete(self, key):
        if self.root:
            node_to_delete = self.root.find(key)
            if node_to_delete:
                if node_to_delete.parent is None:
                    self.root = None
                ext = node_to_delete.delete()
                self.size -= 1
                return ext.item
