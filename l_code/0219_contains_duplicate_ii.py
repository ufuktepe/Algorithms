def contains_nearby_duplicate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: bool
    """
    if k == 0:
        return False

    hashmap = {}

    for i, num in enumerate(nums):
        if num in hashmap:
            j = hashmap[num]
            if i - j <= k:
                return True
        hashmap[num] = i
    return False


def test_success():
    nums = [1, 2, 1, 3, 4]
    k = 2
    assert contains_nearby_duplicate(nums, k) == True


def test_failure():
    nums = [1, 2, 5, 3, 1]
    k = 2
    assert contains_nearby_duplicate(nums, k) == False