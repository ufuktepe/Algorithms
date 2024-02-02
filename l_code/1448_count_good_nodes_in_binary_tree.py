from node import get_balanced_bst


# Time: O(n)  Space: O(n)
def good_nodes(root):
    def traverse(node, max_val):
        if node is None:
            return 0

        new_max_val = max(max_val, node.val)

        count_left = traverse(node.left, new_max_val)
        count_right = traverse(node.right, new_max_val)

        if node.val >= max_val:
            return count_left + count_right + 1
        else:
            return count_left + count_right

    return traverse(root, float('-inf'))


def test():
    root = get_balanced_bst(7)
    assert good_nodes(root) == 3