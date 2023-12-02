from node import Node


# Time: O(N)  Space: O(log(N))
def sorted_array_to_bst(nums):
    def get_balanced_bst(vals, low, high):
        if low > high:
            return None

        mid = (low + high) // 2

        root = Node(vals[mid])
        root.left = get_balanced_bst(vals, low, mid - 1)
        root.right = get_balanced_bst(vals, mid + 1, high)

        return root

    return get_balanced_bst(nums, 0, len(nums) - 1)


def is_balanced(root):
    def evaluate(node):
        if node is None:
            return True, -1

        is_balanced_left, h_left = evaluate(node.left)
        if not is_balanced_left:
            return False, 0
        is_balanced_right, h_right = evaluate(node.right)
        if not is_balanced_right:
            return False, 0

        is_balanced = abs(h_left - h_right) < 2
        height = max(h_left, h_right) + 1
        return is_balanced, height

    return evaluate(root)[0]


def test():
    nums1 = [i+1 for i in range(15)]
    nums2 = [i + 1 for i in range(6)]
    nums3 = [i + 1 for i in range(35)]
    nums4 = [i + 1 for i in range(59)]
    assert is_balanced(sorted_array_to_bst(nums1))
    assert is_balanced(sorted_array_to_bst(nums2))
    assert is_balanced(sorted_array_to_bst(nums3))
    assert is_balanced(sorted_array_to_bst(nums4))