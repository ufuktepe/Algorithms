import heapq


def findKthLargest(nums, k):
    heap = []

    # O(N)
    for num in nums:
        heapq.heappush(heap, -num)

    # O(k*log(N))
    res = None
    for _ in range(k):
        res = heapq.heappop(heap)

    return res * -1


def test_1():
    arr = [5, 3, 4, 7, 6, 9, 1, 8, 2]
    k = 2
    assert findKthLargest(arr, k) == 8


def test_2():
    arr = [1, 2, 1]
    k = 2
    assert findKthLargest(arr, k) == 1


def test_3():
    arr = [1, 1]
    k = 2
    assert findKthLargest(arr, k) == 1