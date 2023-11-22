from node import Node


def build_tree(inorder, postorder):

    idx_map = {val: idx for idx, val in enumerate(inorder)}

    def traverse(start_idx, end_idx):
        val = postorder[-1]
        idx = idx_map[val]

        if not (start_idx <= idx <= end_idx):
            return None

        postorder.pop()
        root = Node(val)

        root.right = traverse(idx + 1, end_idx)
        root.left = traverse(start_idx, idx - 1)

        return root

    return traverse(0, len(inorder) - 1)



a1 = Node(1)
a2 = Node(2)
a3 = Node(3)
a4 = Node(4)
a5 = Node(5)
a6 = Node(6)
a7 = Node(7)
a8 = Node(8)
a9 = Node(9)

a8.left, a8.right = a7, a9
a5.left = a4
a6.left, a6.right = a5, a8
a1.right = a2
a3.left, a3.right = a1, a6

in_order = [1, 2, 3, 4, 5, 6, 7, 8, 9]
post_order = [2, 1, 4, 5, 7, 9, 8, 6, 3]
build_tree(in_order, post_order)

