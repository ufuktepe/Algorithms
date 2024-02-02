import heapq
from collections import defaultdict


def peek_at_max_heap(pq, removed):
    while pq and removed[-pq[0]] > 0:
        removed[-pq[0]] -= 1
        heapq.heappop(pq)

    return -pq[0] if pq else None


def get_skyline(buildings):
    # buildings = [[left, right, height]]
    points = []

    for left, right, height in buildings:
        points.append((left, -height))
        points.append((right, height))

    points.sort()

    contour = []
    pq = [0]  # Max heap
    removed = defaultdict(int)

    for x, height in points:
        if height < 0:
            # Start of a building
            height = abs(height)
            max_height = peek_at_max_heap(pq, removed)
            if height > max_height:
                contour.append((x, -1 * pq[0]))
                contour.append((x, height))
            heapq.heappush(pq, -height)

        else:
            # End of a building
            max_height = peek_at_max_heap(pq, removed)
            removed[height] += 1
            new_max_height = peek_at_max_heap(pq, removed)
            # pq.remove(-height)
            # heapq.heapify(pq)
            if max_height > new_max_height:
                contour.append((x, height))
                contour.append((x, -1 * pq[0]))

    res = []
    prev_x = None
    for x, height in contour:
        if x == prev_x:
            res.append([x, height])
        prev_x = x

    return res


def test():
    buildings = [[3, 7, 2], [5, 9, 1]]
    assert get_skyline(buildings) == [[3, 2], [7, 1], [9, 0]]


def test_2():
    buildings = [[3, 7, 1], [5, 9, 2]]
    assert get_skyline(buildings) == [[3, 1], [5, 2], [9, 0]]


def test_3():
    buildings = [[3, 5, 1], [5, 7, 2]]
    assert get_skyline(buildings) == [[3, 1], [5, 2], [7, 0]]


def test_4():
    buildings = [[3, 5, 2], [5, 7, 1]]
    assert get_skyline(buildings) == [[3, 2], [5, 1], [7, 0]]


def test_5():
    buildings = [[1, 2, 1], [1, 3, 2], [4, 5, 2]]
    assert get_skyline(buildings) == [[1, 2], [3, 0], [4, 2], [5, 0]]