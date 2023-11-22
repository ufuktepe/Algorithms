def binary_search(nums, target):
    left = 0
    right = len(nums)

    while left < right:
        mid = (right + left) // 2
        if target == nums[mid]:
            return mid
        elif target < nums[mid]:
            right = mid
        else:
            left = mid + 1
    return -1


def test_1():
    nums = [0, 1, 2, 3, 4]
    target = 4
    assert binary_search(nums, target) == target
    target = 0
    assert binary_search(nums, target) == target
    target = -9
    assert binary_search(nums, target) == -1
    target = 19
    assert binary_search(nums, target) == -1
