def find_min(nums):
    last = nums[-1]
    left = 0
    while left < len(nums) - 1 and nums[left] == last:
        left += 1

    if nums[left] < last or left == len(nums) - 1:
        return nums[left]

    right = len(nums) - 1

    while left < right:
        mid = (left + right) // 2
        if nums[mid] <= last:
            right = mid
        else:
            left = mid + 1

    return nums[left]


def test_1():
    nums = [1, 1, 2, 3, 3, 4]
    assert find_min(nums) == 1
    nums = [3, 4, 1, 1, 2]
    assert find_min(nums) == 1
    nums = [3, 3, 4, 1, 1, 3]
    assert find_min(nums) == 1
    nums = [3, 3, 4, 1, 1]
    assert find_min(nums) == 1
    nums = [1, 1, 1, 1, 1]
    assert find_min(nums) == 1
    nums = [2, 2, 2, 1, 2]
    assert find_min(nums) == 1