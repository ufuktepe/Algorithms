import heapq


# Time: O(N + k*log(N))  Space: O(N + k)
def k_closest_points_to_origin(points, k):
    dist = []

    # O(N)
    for x, y in points:
        d = x ** 2 + y ** 2
        dist.append((d, x, y))

    # O(N)
    heapq.heapify(dist)

    # O(k*log(N))
    res = []
    while k:
        d, x, y = heapq.heappop(dist)  # O(log(N))
        res.append([x, y])
        k -= 1

    return res


def test_1():
    points = [[1, 2]]
    k = 1
    assert k_closest_points_to_origin(points, k) == [[1, 2]]


def test_2():
    points = [[1, 2], [3, 4], [7, 8], [1, 1]]
    k = 3
    assert k_closest_points_to_origin(points, k) == [[1, 1], [1, 2], [3, 4]]