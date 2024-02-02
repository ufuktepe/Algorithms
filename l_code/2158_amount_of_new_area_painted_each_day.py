import heapq


def peek_at_min_pq(pq, removed):
    while pq and pq[0] in removed:
        heapq.heappop(pq)

    return pq[0] if pq else None


# Time: O(n*log(n))  Space: O(n)
def amount_painted(paint):
    # O(n)
    worklog = [0] * len(paint)

    # O(n)
    events = []
    for i, (start, end) in enumerate(paint):
        events.append((start, 's', i))
        events.append((end, 'e', i))

    # O(n*log(n))
    events.sort()
    pq = []
    last_x = events[0][0]
    removed = set()

    for x, pos, day in events:
        if pos == 's':
            other_day = peek_at_min_pq(pq, removed)    # O(log(n))
            if other_day and other_day > day:
                worklog[other_day] += x - last_x
                last_x = x
            elif other_day is None:
                last_x = x
            heapq.heappush(pq, day)  # O(log(n))

        else:
            if day == peek_at_min_pq(pq, removed):    # O(log(n))
                worklog[pq[0]] += x - last_x
                last_x = x
            removed.add(day)

    return worklog


def test():
    paint = [[1, 5], [7, 9], [3, 11]]
    assert amount_painted(paint) == [4, 2, 4]


def test_2():
    paint = [[1,4],[4,7],[5,8]]
    assert amount_painted(paint) == [3, 3, 1]


def test_3():
    paint = [[1,5],[2,4]]
    assert amount_painted(paint) == [4, 0]