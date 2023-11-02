def get_map(nums):
    hashmap = {}
    for num in nums:
        if num in hashmap:
            hashmap[num] += 1
        else:
            hashmap[num] = 1
    return hashmap


# First attempt
# Length of nums1 is M and nums2 is N.
# Runtime: O(M+N) Space: O(M+N)
def intersect(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    map1 = get_map(nums1)
    map2 = get_map(nums2)
    output = []

    for num, count in map1.items():
        if num in map2:
            for _ in range(min(count, map2[num])):
                output.append(num)
    return output


# Runtime: O(M+N) Space: O(min(M, N))
def intersect_v2(nums1, nums2):
    if len(nums1) > len(nums2):
        return intersect_v2(nums2, nums1)

    output = []
    count = {}
    for num in nums1:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1

    for num in nums2:
        if num in count and count[num] > 0:
            output.append(num)
            count[num] -= 1

    return output


def test_1_common_num():
    nums1 = [1, 2, 3, 4]
    nums2 = [5, 6, 1, 5]
    assert intersect(nums1, nums2) == [1]


def test_2_common_nums():
    nums1 = [1, 2, 3, 4]
    nums2 = [5, 2, 1, 5]
    assert sorted(intersect(nums1, nums2)) == [1, 2]