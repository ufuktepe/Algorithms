# Time: O(log(N))  Space: O(1)
def find_pivot(nums):
    left = 0
    right = len(nums) - 1
    last = nums[-1]

    while left <= right:
        mid = (left + right) // 2

        if last < nums[mid]:
            left = mid + 1
        elif last >= nums[mid]:
            right = mid - 1

    return left


# Time: O(log(N))  Space: O(1)
def search(nums, target):
    k = find_pivot(nums)
    nums = nums[k:] + nums[:k]

    left = 0
    right = len(nums) - 1
    # O(log(N))
    while left <= right:
        mid = (left + right) // 2
        if target == nums[mid]:
            return (mid + k) % len(nums)
        elif target < nums[mid]:
            right = mid - 1
        else:
            left = mid + 1

    return -1


def search_v2(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if target == nums[mid]:
            return mid
        elif nums[left] <= nums[mid]:  # Implies nums is sorted between left and mid
            if nums[left] <= target < nums[mid]:
                right = mid - 1  # Discard the right half
            else:
                left = mid + 1   # Discard the left half
        else:  # Implies nums is sorted between mid and right
            if nums[mid] < target <= nums[right]:
                left = mid + 1   # Discard the left half
            else:
                right = mid - 1  # Discard the right half
    return -1


def test_1():
    nums = [4, 5, 6, 0, 1, 2, 3]
    target = 6
    assert search_v2(nums, target) == 2
    target = 9
    assert search_v2(nums, target) == -1
    target = 0
    assert search_v2(nums, target) == 3
    nums = [3, 1]
    target = 1
    assert search_v2(nums, target) == 1