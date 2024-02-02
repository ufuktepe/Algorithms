import heapq


# Time: O(n*log(n))  Space: O(n)
def taps(n, ranges):
    intervals = []
    # O(n)
    for i, range in enumerate(ranges):
        intervals.append((i - range, i + range))

    # O(n*log(n))
    intervals.sort()

    pq = []  # max heap
    x = i = count = 0

    # O(n*log(n))
    while x < n:
        while i < len(intervals) and intervals[i][0] <= x:
            heapq.heappush(pq, -intervals[i][1])
            i += 1

        if not pq:
            return -1

        end = heapq.heappop(pq) * -1
        if end < x:
            return -1

        count += 1
        x = end

    return count


# Time: O(n)  Space: O(n)
def taps_v2(n, ranges):
    max_reach = [i for i in range(n + 1)]

    for i, rng in enumerate(ranges):
        start = max(0, i - rng)
        end = i + rng
        max_reach[start] = max(max_reach[start], end)

    x = last_x = count = 0
    cur_reach = max_reach[0]
    while x < n:
        for i in range(last_x, x + 1):
            cur_reach = max(cur_reach, max_reach[i])
        if x == cur_reach:
            return -1

        last_x = x
        x = cur_reach
        count += 1

    return count


def test():
    n = 5
    ranges = [4,1,1,1,1,1]
    assert taps_v2(n, ranges) == 2