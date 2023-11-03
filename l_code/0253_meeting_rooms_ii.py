import heapq


# Time: O(N*log(N))  Space: O(N)
def min_meeting_rooms(intervals):
    pq_rooms = [0]
    heapq.heapify(intervals)  # O(N)

    # O(N*log(N))
    while intervals:
        start, end = heapq.heappop(intervals)  # O(log(N))

        if pq_rooms[0] <= start:
            heapq.heappop(pq_rooms)            # O(log(N))

        heapq.heappush(pq_rooms, end)          # O(log(N))

    return len(pq_rooms)


def test_1():
    intervals = [[1, 10]]
    assert min_meeting_rooms(intervals) == 1


def test_2():
    intervals = [[1, 7], [7, 9], [2, 4], [5, 6], [8, 9]]
    assert min_meeting_rooms(intervals) == 2