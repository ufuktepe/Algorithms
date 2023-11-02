def two_sum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    hashmap = {num: i for i, num in enumerate(nums)}
    for i, num in enumerate(nums):
        r = target - num
        if r in hashmap and i != hashmap[r]:
            return [i, hashmap[r]]


def test_2_items():
    nums = [1, 3]
    target = 4
    assert two_sum(nums, target) == [0, 1]


def test_3_items():
    nums = [3, 2, 4]
    target = 6
    assert two_sum(nums, target) == [1, 2]