import heapq


def min_effort(heights):
    n = len(heights)
    m = len(heights[0])

    # O(M*N)
    effort = [[float('inf') for j in range(m)] for i in range(n)]
    effort[0][0] = 0

    pq = [(0, 0, 0)]  # effort, i, j

    while pq:
        cur_effort, i, j = heapq.heappop(pq)

        for x, y in get_adj(heights, i, j):
            if effort[x][y] > max(abs(heights[i][j] - heights[x][y]), cur_effort):
                effort[x][y] = max(abs(heights[i][j] - heights[x][y]), cur_effort)
                heapq.heappush(pq, (effort[x][y], x, y))

    return effort[n - 1][m - 1]


def get_adj(heights, i, j):
    dirs = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
    adj = []
    for x, y in dirs:
        if is_valid(heights, x, y):
            adj.append((x, y))
    return adj


def is_valid(heights, i, j):
    if 0 <= i < len(heights) and 0 <= j < len(heights[0]):
        return True
    return False


def test():
    heights = [[1, 2, 2], [3, 8, 2], [5, 3, 5]]
    assert min_effort(heights) == 2


def test_2():
    heights = [[1, 2, 3],
               [3, 8, 4],
               [5, 3, 5]]
    assert min_effort(heights) == 1