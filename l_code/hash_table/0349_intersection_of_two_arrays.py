def intersection(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    unique_nums1 = set(nums1)
    res = set()

    for num in nums2:
        if num in unique_nums1:
            res.add(num)

    return list(res)


def test_no_intersection():
    nums1 = [1, 2, 3]
    nums2 = [4, 5, 6]
    assert intersection(nums1, nums2) == []


def test_intersection():
    nums1 = [1, 2, 3]
    nums2 = [4, 1, 5]
    assert intersection(nums1, nums2) == [1]