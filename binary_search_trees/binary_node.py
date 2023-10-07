class BinaryNode:
    def __init__(self, item):
        self.item = item
        self.parent = None
        self.left = None
        self.right = None

    def subtree_iter(self):
        """Yield nodes in the subtree in traversal order."""
        if self.left:
            yield from self.left.subtree_iter()
        yield self
        if self.right:
            yield from self.right.subtree_iter()

    def get_first_node_in_subtree(self):
        """Return the first node in the subtree in traversal order."""
        if self.left:
            return self.left.get_first_node_in_subtree()
        return self

    def get_last_node_in_subtree(self):
        """Return the last node in the subtree in traversal order."""
        if self.right:
            return self.right.get_last_node_in_subtree()
        return self

    def get_successor(self):
        """Return the next node in traversal order."""
        if self.right:
            return self.right.get_first_node_in_subtree()
        child = self
        while child.parent and child.parent.left is not child:
            child = child.parent
        return child.parent

    def get_predecessor(self):
        """Return the previous node in traversal order."""
        if self.left:
            return self.left.get_last_node_in_subtree()
        child = self
        while child.parent and child.parent.right is not child:
            child = child.parent
        return child.parent

    def insert_before(self, node):
        """Insert the given node before this node in traversal order."""
        if self.left:
            last_node = self.left.get_last_node_in_subtree()
            last_node.right = node
            node.parent = last_node
        else:
            self.left = node
            node.parent = self

    def insert_after(self, node):
        """Insert the given node after this node in traversal order."""
        if self.right:
            first_node = self.right.get_first_node_in_subtree()
            first_node.left = node
            node.parent = first_node
        else:
            self.right = node
            node.parent = self

    def delete(self):
        """Delete this node."""
        if self.right is None and self.left is None:
            if self.parent is not None:
                if self.parent.left is self:
                    self.parent.left = None
                else:
                    self.parent.right = None
            return self
        elif self.left is not None:
            node_to_delete = self.get_predecessor()
        else:
            node_to_delete = self.get_successor()

        self.item, node_to_delete.item = node_to_delete.item, self.item
        return node_to_delete.delete()


if __name__ == '__main__':

    a = BinaryNode('a')
    b = BinaryNode('b')
    c = BinaryNode('c')
    d = BinaryNode('d')
    e = BinaryNode('e')

    a.parent = b
    c.parent = b
    b.parent = d
    e.parent = d

    d.left = b
    d.right = e
    b.left = a
    b.right = c

    node = d
    # node_before = node.get_predecessor()
    # node_after = node.get_successor()
    # if node_before:
    #     print(f'predecessor: {node_before.item}')
    # if node_after:
    #     print(f'successor: {node_after.item}')

    node.delete()

    for n in d.subtree_iter():
        print(n.item)