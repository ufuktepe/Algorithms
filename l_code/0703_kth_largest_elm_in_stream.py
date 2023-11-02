import heapq


# Build Time: O(N*log(k))
# Time for addition: O(log(k))
# Space: O(k)
class KthLargest:
    def __init__(self, k, nums):
        self.k = k
        self.heap = []

        # O(N*log(k))
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        # O(log(k))
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            # O(log(k))
            heapq.heappop(self.heap)

        return self.heap[0]


def test_1():
    nums = [1, 6, 3, 2, 5, 4]
    k = 3
    kl = KthLargest(k, nums)
    assert kl.add(3) == 4
    assert kl.add(7) == 5
