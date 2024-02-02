def find(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return True
        elif nums[mid] < nums[right]:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
        elif nums[left] < nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        elif nums[left] == nums[mid] == nums[right]:
            left += 1
        elif nums[left] == nums[mid]:
            left = mid + 1  # discard left
        else:
            right = mid - 1 # discard right
    return False


def test():
    nums = [1, 2, 3, 4]
    assert find(nums, 1)
    assert find(nums, 2)
    assert find(nums, 3)
    assert find(nums, 4)


def test_2():
    nums = [4, 1, 2, 3]
    assert find(nums, 1)
    assert find(nums, 2)
    assert find(nums, 3)
    assert find(nums, 4)


def test_3():
    nums = [1, 0, 1, 1, 1]
    assert find(nums, 0)