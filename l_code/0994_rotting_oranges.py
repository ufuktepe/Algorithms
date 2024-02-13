from collections import deque


# Time: O(n*m)  Space: O(n*m)
def orange_rotting(grid):
    q = deque()  # invariant: contains rotten oranges
    m, n = len(grid), len(grid[0])
    fresh_count = 0

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 2:
                q.append((i, j, 0))
            elif grid[i][j] == 1:
                fresh_count += 1

    rotten_count = 0
    max_time = 0
    while q:
        i, j, t = q.popleft()
        max_time = max(max_time, t)

        for x, y in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
            if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                grid[x][y] = 2
                rotten_count += 1
                q.append((x, y, t + 1))

    return max_time if rotten_count == fresh_count else -1


def test():
    grid = [[2, 1, 1, 1],
            [1, 0, 1, 1],
            [2, 0, 1, 2]]

    assert orange_rotting(grid) == 2


def test_2():
    grid = [[2, 1, 0, 1],
            [1, 0, 1, 0],
            [2, 0, 1, 2]]

    assert orange_rotting(grid) == -1