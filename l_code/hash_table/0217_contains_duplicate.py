def contains_duplicate(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    unique_nums = set()
    for num in nums:
        if num in unique_nums:
            return True
        unique_nums.add(num)
    return False


# Using array
def contains_duplicate_v2(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    nums.sort()
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            return True
    return False


def test_unique_1_item():
    nums = [1]
    assert contains_duplicate_v2(nums) == False


def test_unique_2_items():
    nums = [1, 2]
    assert contains_duplicate_v2(nums) == False


def test_duplicate_2_items():
    nums = [1, 1]
    assert contains_duplicate_v2(nums) == True