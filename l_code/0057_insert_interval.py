import heapq


# Time: O(n*log(n))  Space: O(n)
def insert(intervals, newInterval):
    events = [(newInterval[0], 0), (newInterval[1], 1)]
    for start, end in intervals:
        events.append((start, 0))
        events.append((end, 1))

    events.sort()
    pq = []  # Max heap
    res = []

    for t, pos in events:
        if pos == 0:
            heapq.heappush(pq, -t)
        else:
            start = heapq.heappop(pq) * -1
            if not pq:
                res.append([start, t])

    return res


def insert_v2(intervals, newInterval):
    for i, (start, end) in enumerate(intervals):
        if start > newInterval[0]:
            intervals.insert(i, newInterval)
            break
    else:
        intervals.append(newInterval)

    i = 0
    res = []

    while i < len(intervals):
        cur_interval = intervals[i]
        i += 1

        while i < len(intervals) and intervals[i][0] <= cur_interval[1]:
            cur_interval[1] = max(cur_interval[1], intervals[i][1])
            i += 1

        res.append(cur_interval)

    return res


def test():
    intervals = [[1, 3], [4, 5], [7, 9]]
    newInterval = [2, 7]
    assert insert_v2(intervals, newInterval) == [[1, 9]]