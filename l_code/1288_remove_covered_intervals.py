import heapq


def peek_at_pq(pq, removed):
    while pq and (pq[0][1] in removed):
        heapq.heappop(pq)
    return pq[0] if pq else None


# Time O(n*log(n))  Space: O(n)
def remove_covered(intervals):
    events = []
    for i, (s, e) in enumerate(intervals):
        events.append((s, 0, 's', i))
        events.append((e, -s, 'e', i))
    events.sort()

    pq = []  # Min heap
    removed = set()
    count = 0

    for time1, time2, pos, i in events:
        if pos == 's':
            heapq.heappush(pq, (time1, i))
        else:
            removed.add(i)
            min_item = peek_at_pq(pq, removed)
            if min_item is None or -time2 < min_item[0]:
                count += 1

    return count


def test():
    intervals = [[1, 4], [3, 6], [2, 8]]
    assert remove_covered(intervals) == 2