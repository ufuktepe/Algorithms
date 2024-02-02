import heapq


# Time: O(n*log(n))  Space: O(n)
def merge(intervals):
    events = []
    for start, end in intervals:
        events.append((start, 0))
        events.append((end, 1))
    events.sort()  # O(n*log(n))
    pq = []  # max heap
    res = []

    # O(n*log(n))
    for t, pos in events:
        if pos == 0:
            heapq.heappush(pq, -t)
        else:
            start = heapq.heappop(pq) * -1
            if not pq:
                res.append([start, t])

    return res


def test():
    intervals = [[1, 4], [4, 6]]
    assert merge(intervals) == [[1, 6]]