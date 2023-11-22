import heapq


# Space: O(N)
class MedianFinder:
    def __init__(self):
        self.first = []
        self.second = []

    # O(log(N))
    def addNum(self, num: int) -> None:
        # adds the integer num from the data stream to the data structure.
        if not self.first or num < -self.first[0]:
            heapq.heappush(self.first, -num)
        else:
            heapq.heappush(self.second, num)

        if len(self.first) - len(self.second) > 1:
            item = -heapq.heappop(self.first)
            heapq.heappush(self.second, item)
        elif len(self.second) - len(self.first) > 1:
            item = -heapq.heappop(self.second)
            heapq.heappush(self.first, item)

    # O(1)
    def findMedian(self) -> float:
        if len(self.first) > len(self.second):
            return -self.first[0]
        elif len(self.second) > len(self.first):
            return self.second[0]
        else:
            return (-self.first[0] + self.second[0]) / 2

def test_1():
    mf = MedianFinder()
    mf.addNum(1)
    mf.addNum(2)
    assert mf.findMedian() == 1.5
    mf.addNum(3)
    assert mf.findMedian() == 2