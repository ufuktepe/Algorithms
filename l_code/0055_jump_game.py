# Time: O(n)  Space: O(n)
def can_jump(nums):
    visited = [False] * len(nums)

    def visit(i):
        visited[i] = True

        if i == len(nums) - 1:
            return True

        for j in range(1, nums[i] + 1):
            if not visited[i + j] and visit(i + j):
                return True

        return False

    return visit(0)


def test():
    nums = [2, 0, 1, 0]
    assert can_jump(nums)


def test_2():
    nums = [3, 2, 1, 0, 1]
    assert can_jump(nums) is False