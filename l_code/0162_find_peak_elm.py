def find_peak_elm(nums):
    left = 0
    right = len(nums) - 1

    while left < right:
        mid = (left + right) // 2

        if nums[mid] < nums[mid + 1]:
            left = mid + 1
        else:
            right = mid

    return left

def test_1():
    nums = [1, 2, 3, 5, 7]
    assert find_peak_elm(nums) == 4
    nums = [3, 2]
    assert find_peak_elm(nums) == 0
    nums = [5, 4, 3, 4, 5]
    assert find_peak_elm(nums) == 4
    nums = [1, 3, 5, 7, 9, 2]
    assert find_peak_elm(nums) == 4