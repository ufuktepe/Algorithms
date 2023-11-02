from collections import deque


def num_islands(grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """
    n = 0
    seen = set()

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (i, j) in seen:
                continue
            seen.add((i, j))
            if grid[i][j] == '1':
                bfs(i, j, seen, grid)
                n += 1
    return n


def bfs(i, j, seen, grid):
    q = deque()
    q.append((i, j))

    while q:
        x, y = q.popleft()

        for nx, ny in get_neighbors(grid, x, y):
            if (nx, ny) not in seen:
                seen.add((nx, ny))
                q.append((nx, ny))


def get_neighbors(grid, i, j):
    neighbors = []
    if i - 1 >= 0 and grid[i - 1][j] == '1':
        neighbors.append((i - 1, j))
    if i + 1 < len(grid) and grid[i + 1][j] == '1':
        neighbors.append((i + 1, j))
    if j - 1 >= 0 and grid[i][j - 1] == '1':
        neighbors.append((i, j - 1))
    if j + 1 < len(grid[i]) and grid[i][j + 1] == '1':
        neighbors.append((i, j + 1))

    return neighbors


def test_1_island():
    grid = [
        ['1', '1', '0'],
        ['1', '1', '0'],
        ['0', '0', '0']
    ]
    assert num_islands(grid) == 1


def test_2_islands():
    grid = [
        ['1', '1', '0', '0'],
        ['1', '0', '0', '0'],
        ['1', '0', '0', '1']
    ]
    assert num_islands(grid) == 2