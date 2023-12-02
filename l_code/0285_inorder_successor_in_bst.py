from node import Node


# Time: O(N)  Space: O(N) since BST might not be balanced (i.e. has a linked list structure)
def inorder_successor(root, p):
    def find_successor(node, successor=None):
        if node is None:
            return successor

        if node.val > p.val:
            successor = node
            return find_successor(node.left, successor)

        else:
            return find_successor(node.right, successor)

    return find_successor(root)

def test():
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n6 = Node(6)

    n5.left, n5.right = n3, n6
    n3.left, n3.right = n2, n4
    n2.left = n1

    assert inorder_successor(n5, n2) == n3