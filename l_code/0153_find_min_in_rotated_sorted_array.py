# Time: O(log(N))  Space: O(1)
def find_min(nums):
    left = 0
    right = len(nums) - 1
    last = nums[-1]

    # O(log(N))
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > last:
            left = mid + 1
        else:
            right = mid
    return nums[left]

def test_1():
    nums = [3, 4, 5, 1, 2]
    assert find_min(nums) == 1
    nums = [1, 2, 3]
    assert find_min(nums) == 1
    nums = [7, 8, 9, 0, 2]
    assert find_min(nums) == 0