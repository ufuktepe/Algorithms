import collections
from collections import defaultdict
import heapq
from heapq import *


# First attempt
# Time: O(N) Space: O(N)
def top_k_frequent(nums, k):
    freq_to_nums = defaultdict(list)  # Maps frequencies to the list of nums w/ that frequency
    nums_to_freqs = defaultdict(int)

    # O(N)
    for num in nums:
        nums_to_freqs[num] += 1

    # O(N)
    for num, freq in nums_to_freqs.items():
        freq_to_nums[freq].append(num)

    # O(N)
    res = []
    i = len(nums)
    while len(res) < k:
        if freq_to_nums[i]:
            res.extend(freq_to_nums[i])
            i -= 1

    return res


# Using minheap
# Time: O(N*log(k)) Space: O(N + 2k)
def top_k_frequent_with_heap(nums, k):
    # O(N)
    nums_to_freqs = collections.Counter(nums)
    heap = []

    # O(N*log(k))
    for num, freq in nums_to_freqs.items():
        heappush(heap, [freq, num])
        if len(heap) > k:
            heappop(heap)

    res = []

    # O(k*log(k))
    while heap:
        res.append(heappop(heap)[1])
    return res


# Using maxheap
# Time: O(k*log(N)) Space: O(2n + k)
def top_k_frequent_with_heap_v2(nums, k):
    hmap = defaultdict(int)

    # O(N)
    for num in nums:
        hmap[num] += 1

    # O(N)
    heap = [(-freq, num) for num, freq in hmap.items()]

    # O(N)
    heapq.heapify(heap)

    res = []

    # O(k*log(N))
    for _ in range(k):
        res.append(heapq.heappop(heap)[1])

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