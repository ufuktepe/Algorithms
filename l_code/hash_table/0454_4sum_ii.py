from collections import defaultdict


def four_sum_count(nums1, nums2, nums3, nums4):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :type nums3: List[int]
    :type nums4: List[int]
    :rtype: int
    """
    hmap = defaultdict(int)
    for num3 in nums3:
        for num4 in nums4:
            hmap[(num3+num4)*-1] += 1

    n = 0

    for num1 in nums1:
        for num2 in nums2:
            n += hmap[num1 + num2]

    return n


def test_1():
    nums1 = [0]
    nums2 = [0]
    nums3 = [0]
    nums4 = [0]

    assert four_sum_count(nums1, nums2, nums3, nums4) == 1


def test_2():
    nums1 = [10, 20]
    nums2 = [100, 101]
    nums3 = [-10, -20]
    nums4 = [-100, -101]

    assert four_sum_count(nums1, nums2, nums3, nums4) == 4


def test_3():
    nums1 = [0, 1, -1]
    nums2 = [-1, 1, 0]
    nums3 = [0, 0, 1]
    nums4 = [-1, 1, 1]

    assert four_sum_count(nums1, nums2, nums3, nums4) == 17
