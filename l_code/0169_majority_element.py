from collections import defaultdict


# Time: O(N)  Space: O(N)
def majority_element(nums):
    frequency = defaultdict(int)

    threshold = len(nums) // 2

    for num in nums:
        frequency[num] += 1
        if frequency[num] > threshold:
            return num


def test_odd():
    nums = [1, 2, 2]
    assert majority_element(nums) == 2


def test_even():
    nums = [10, 12, 12, 14, 14, 14, 14, 14]
    assert majority_element(nums) == 14