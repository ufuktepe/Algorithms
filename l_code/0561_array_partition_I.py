def arrayPairSum(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    nums.sort()
    res = 0

    for i in range(0, len(nums), 2):
        res += nums[i]
    return res


def test_n_is_1():
    nums = [1, 2]
    assert arrayPairSum(nums) == 1


def test_n_is_2():
    nums = [1, 2, 3, 4]
    assert arrayPairSum(nums) == 4


def test_n_is_3():
    nums = [6, 2, 6, 5, 1, 2]
    assert arrayPairSum(nums) == 9