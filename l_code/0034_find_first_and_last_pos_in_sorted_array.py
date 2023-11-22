def find_last_index(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if target < nums[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return right if nums[right] == target else -1


def find_first_index(nums, target):
    left = 0
    right = len(nums) - 1

    while left < right:
        mid = (left + right) // 2
        if nums[mid] >= target:
            right = mid
        else:
            left = mid + 1
    return right if nums[right] == target else -1


def search_range(nums, target):
    first = find_first_index(nums, target)
    if first == -1:
        return [-1, -1]
    last = find_last_index(nums, target)
    return [first, last]


def test_1():
    nums = [1, 2, 3, 3, 3, 3, 4, 5]
    target = 3
    assert search_range(nums, target) == [2, 5]
    target = 6
    assert search_range(nums, target) == [-1, -1]
    target = 5
    assert search_range(nums, target) == [7, 7]