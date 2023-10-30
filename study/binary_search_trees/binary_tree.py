from binary_node import BinaryNode


class BinaryTree:
    def __init__(self, Node_Type=BinaryNode):
        self.root = None
        self.size = 0
        self.Node_Type = Node_Type

    def __len__(self):
        return self.size

    def __iter__(self):
        if self.root is None:
            return None
        for node in self.root.subtree_iter():
            yield node.item
