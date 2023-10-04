def height(node):
    if node is None:
        return -1
    return node.height


class BinaryNode:
    def __init__(self, item):
        self.item = item
        self.parent = None
        self.left = None
        self.right = None
        self.height = None
        self.update_height()

    def update_height(self):
        """Update the height of the tree. O(1)"""
        self.height = 1 + max(height(self.left), height(self.right))

    def subtree_iter(self):
        """Yield nodes in the subtree in traversal order. O(n)"""
        if self.left:
            yield from self.left.subtree_iter()
        yield self
        if self.right:
            yield from self.right.subtree_iter()

    def get_first_node_in_subtree(self):
        """Return the first node in the subtree in traversal order. O(h)"""
        if self.left:
            return self.left.get_first_node_in_subtree()
        return self

    def get_last_node_in_subtree(self):
        """Return the last node in the subtree in traversal order. O(h)"""
        if self.right:
            return self.right.get_last_node_in_subtree()
        return self

    def get_successor(self):
        """Return the next node in traversal order. O(h)"""
        if self.right:
            return self.right.get_first_node_in_subtree()
        child = self
        while child.parent and child.parent.left is not child:
            child = child.parent
        return child.parent

    def get_predecessor(self):
        """Return the previous node in traversal order. O(h)"""
        if self.left:
            return self.left.get_last_node_in_subtree()
        child = self
        while child.parent and child.parent.right is not child:
            child = child.parent
        return child.parent

    def rotate_left(self):
        """Rotate counter clockwise. O(1)"""
        node_a, node_d = self.left, self.right

        if node_d:
            node_c, node_e = node_d.left, node_d.right
            node_d.parent = self.parent
            node_d.left = self
        else:
            node_c = None

        self.parent = node_d
        self.right = node_c

        if node_c:
            node_c.parent = self

    def rotate_right(self):
        """Rotate clockwise. O(1)"""
        node_b, node_e = self.left, self.right

        if node_b:
            node_a, node_c = node_b.left, node_b.right
            node_b.parent = self.parent
            node_b.right = self
        else:
            node_c = None

        self.parent = node_b
        self.left = node_c

        if node_c:
            node_c.parent = self

    def skew(self):
        """Return the height difference between right and left subtrees. O(1)"""
        return height(self.right) - height(self.left)

    def rebalance(self):
        """Rotate based on skew. O(1)"""
        if self.skew() == 2:
            # Tree is right heavy
            if self.right.skew() < 0:
                # Right subtree is left heavy, so rotate it right
                self.right.rotate_right()
            self.rotate_left()
        elif self.skew() == -2:
            # Tree is left heavy
            if self.left.skew() > 0:
                # Left subtree is right heavy, so rotate it left
                self.left.rotate_left()
            self.rotate_right()

    def maintain(self):
        """Rotate, update height, and maintain parent if exists. O(h)"""
        self.rebalance()
        self.update_height()
        if self.parent:
            self.parent.maintain()

    def insert_before(self, node):
        """Insert the given node before this node in traversal order. O(h)"""
        if self.left:
            last_node = self.left.get_last_node_in_subtree()
            last_node.right = node
            node.parent = last_node
        else:
            self.left = node
            node.parent = self
        self.maintain()

    def insert_after(self, node):
        """Insert the given node after this node in traversal order. O(h)"""
        if self.right:
            first_node = self.right.get_first_node_in_subtree()
            first_node.left = node
            node.parent = first_node
        else:
            self.right = node
            node.parent = self
        self.maintain()

    def delete(self):
        """Delete this node. O(h)"""
        if self.right is None and self.left is None:
            if self.parent is not None:
                if self.parent.left is self:
                    self.parent.left = None
                else:
                    self.parent.right = None
                self.parent.maintain()
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

    a.update_height()
    c.update_height()
    b.update_height()
    e.update_height()
    d.update_height()

    d.rotate_right()
    # b.rotate_left()

    # node = d
    # node_before = node.get_predecessor()
    # node_after = node.get_successor()
    # if node_before:
    #     print(f'predecessor: {node_before.item}')
    # if node_after:
    #     print(f'successor: {node_after.item}')

    # node.delete()

    for n in b.subtree_iter():
        print(f'{n.item} -> height: {n.height}')