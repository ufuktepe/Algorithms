# Time: O(n)  Space: O(1)
def first_missing_pos(nums):
    n = len(nums)

    for i in range(n):
        if nums[i] < 0:
            nums[i] = 0

    for i in range(n):
        if nums[i] == 0 or abs(nums[i]) > n:
            continue

        idx = abs(nums[i]) - 1

        if nums[idx] > 0:
            nums[idx] *= -1
        elif nums[idx] == 0:
            nums[idx] = abs(nums[i]) * -1

    for i in range(n):
        if nums[i] >= 0:
            return i + 1

    return n + 1


def test():
    nums = [0, 1, 2]
    assert first_missing_pos(nums) == 3


def test_2():
    nums = [4, 2, 3, 1, 7, 9]
    assert first_missing_pos(nums) == 5