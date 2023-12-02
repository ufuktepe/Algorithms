from node import Node

# Let H be the height of the BST
class BSTIterator:

    # Time: O(H)  Space: O(H)
    def __init__(self, root):
        self.stack = []

        cur = root
        while cur:
            self.stack.append(cur)
            cur = cur.left

    # Time: O(1) amortized
    def next(self):
        # Moves the pointer to the right, then returns the number at the pointer.
        next_node = self.stack.pop()
        cur = next_node.right
        while cur:
            self.stack.append(cur)
            cur = cur.left
        return next_node.val

    # Time: O(1)
    def hasNext(self):
        # Returns true if there exists a number in the traversal to the right of the pointer, otherwise returns false.
        if self.stack:
            return True



def test():
    nodes = [Node(i) for i in range(12)]

    nodes[8].left, nodes[8].right = nodes[5], nodes[10]
    nodes[5].left, nodes[5].right = nodes[1], nodes[7]
    nodes[10].left, nodes[10].right = nodes[9], nodes[11]
    nodes[1].left, nodes[1].right = nodes[0], nodes[3]
    nodes[3].left, nodes[3].right = nodes[2], nodes[4]
    nodes[7].left = nodes[6]

    bst_iterator = BSTIterator(nodes[8])
    assert bst_iterator.hasNext()
    assert bst_iterator.next() == nodes[0].val
    assert bst_iterator.hasNext()
    assert bst_iterator.next() == nodes[1].val
    assert bst_iterator.hasNext()
    assert bst_iterator.next() == nodes[2].val
    assert bst_iterator.hasNext()
    assert bst_iterator.next() == nodes[3].val
    assert bst_iterator.hasNext()
    assert bst_iterator.next() == nodes[4].val
    assert bst_iterator.hasNext()
    assert bst_iterator.next() == nodes[5].val
    assert bst_iterator.hasNext()
    assert bst_iterator.next() == nodes[6].val
    assert bst_iterator.hasNext()
    assert bst_iterator.next() == nodes[7].val