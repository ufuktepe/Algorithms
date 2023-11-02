def findMaxConsecutiveOnes(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    res_overall = 0
    res_cur = 0
    for num in nums:
        if num == 1:
            res_cur += 1
        else:
            if res_overall < res_cur:
                res_overall = res_cur
            res_cur = 0

    if res_overall < res_cur:
        res_overall = res_cur

    return res_overall


def test_n_is_1():
    nums_a = [1]
    nums_b = [0]
    assert findMaxConsecutiveOnes(nums_a) == 1
    assert findMaxConsecutiveOnes(nums_b) == 0


def test_n_is_2():
    nums_a = [1, 0]
    assert findMaxConsecutiveOnes(nums_a) == 1


def test_n_is_10():
    nums_a = [1, 0, 1, 1, 0, 0, 1, 1, 1, 1 ]
    assert findMaxConsecutiveOnes(nums_a) == 4
