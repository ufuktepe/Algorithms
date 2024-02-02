import heapq


def attend(events):
    events.sort()
    pq = []

    count = 0
    day = events[0][0]
    i = 0

    while i < len(events) or pq:
        while i < len(events) and events[i][0] <= day:
            heapq.heappush(pq, events[i][1])
            i += 1

        while pq and pq[0] < day:
            heapq.heappop(pq)

        if pq:
            heapq.heappop(pq)
            count += 1
            day += 1
        else:
            day = events[i][0]


    return count


def test():
    events = [[1, 2], [2, 3], [3, 4], [1, 2]]
    assert attend(events) == 4


def test_2():
    events = [[1, 2], [1, 2], [3, 3], [1, 5], [1, 5]]
    assert attend(events) == 5