import collections
from collections import defaultdict
from heapq import *


# First attempt
# Time: O(n) Space: O(n)
def top_k_frequent(nums, k):
    freq_to_nums = defaultdict(list)  # Maps frequencies to the list of nums w/ that frequency
    nums_to_freqs = defaultdict(int)

    for num in nums:
        nums_to_freqs[num] += 1

    for num, freq in nums_to_freqs.items():
        freq_to_nums[freq].append(num)

    res = []
    i = len(nums)
    while len(res) < k:
        if freq_to_nums[i]:
            res.extend(freq_to_nums[i])
            i -= 1

    return res


# Using heapq
def top_k_frequent_with_heap(nums, k):
    nums_to_freqs = collections.Counter(nums)
    heap = []

    for num, freq in nums_to_freqs.items():
        heappush(heap, [freq, num])
        if len(heap) > k:
            heappop(heap)

    res = []
    while heap:
        res.append(heappop(heap)[1])
    return res


def test_k_is_1():
    nums = [1]
    k = 1
    assert top_k_frequent(nums, k) == [1]


def test_k_is_2():
    nums = [1, 1, 2, 2, 4]
    k = 2
    assert top_k_frequent(nums, k) == [1, 2]


def test_k_is_3():
    nums = [1, 2, 2, 3, 2, 3, 4, 4]
    k = 3
    assert top_k_frequent_with_heap(nums, k) == [2, 3, 4]