# Time: O(log(n)) where n is the num of integers in nums
# Space: O(1)
def get_index(nums, target):
    left, right = 0, len(nums) - 1

    while left < right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    if nums[left] < target:
        return left + 1
    else:
        return left


def test():
    nums = [1]
    target = 2
    assert get_index(nums, target) == 1
    target = 1
    assert get_index(nums, target) == 0
    target = 0
    assert get_index(nums, target) == 0


def test_2():
    nums = [2, 5]
    target = 1
    assert get_index(nums, target) == 0
    target = 2
    assert get_index(nums, target) == 0
    target = 3
    assert get_index(nums, target) == 1
    target = 5
    assert get_index(nums, target) == 1
    target = 6
    assert get_index(nums, target) == 2