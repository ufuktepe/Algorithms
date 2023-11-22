# Binary search solution
def find_duplicate(nums):
    left, right = 1, len(nums) - 1
    duplicate = None
    while left <= right:
        cur = (left + right) // 2

        count = sum([1 for num in nums if num <= cur])

        if count > cur:
            duplicate = cur
            right = cur - 1
        else:
            left = cur + 1

    return duplicate


# Linked list solution
def find_duplicate_v2(nums):
    slow = fast = nums[0]

    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]

    return fast

def test_1():
    nums = [3, 2, 4, 2, 1]
    assert find_duplicate_v2(nums) == 2
    nums = [1, 3, 3, 4, 3]
    assert find_duplicate_v2(nums) == 3
    nums = [3, 3, 3, 3, 3]
    assert find_duplicate_v2(nums) == 3
    nums = [1, 1]
    assert find_duplicate_v2(nums) == 1