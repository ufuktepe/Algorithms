from collections import deque

# Time: O(m*n)  Space: O(m*n)
def oranges_rotting(grid):
    m = len(grid)
    n = len(grid[0])

    n_fresh = 0

    # O(m*n)
    visited = [[0 for j in range(n)] for i in range(m)]

    q = deque()

    # O(m*n)
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                n_fresh += 1
            if grid[i][j] == 2:
                for x, y in get_fresh_neighbors(grid, i, j):
                    if not visited[x][y]:
                        visited[x][y] = 1
                        q.append((x, y))

    mins = 0
    # O(m*n)
    while q:
        mins += 1
        new_q = deque()
        while q:
            x, y = q.popleft()
            grid[x][y] = 2
            n_fresh -= 1
            for nx, ny in get_fresh_neighbors(grid, x, y):
                if not visited[nx][ny]:
                    visited[nx][ny] = 1
                    new_q.append((nx, ny))

        q = new_q

    return mins if n_fresh == 0 else -1


def oranges_rotting_v2(grid):
    m = len(grid)
    n = len(grid[0])

    n_fresh = 0
    q = deque()

    # O(m*n)
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                n_fresh += 1
            if grid[i][j] == 2:
                q.append((i, j))

    mins = 0
    # O(m*n)
    while q and n_fresh > 0:
        mins += 1
        new_q = deque()
        while q:
            x, y = q.popleft()

            for nx, ny in get_fresh_neighbors(grid, x, y):
                grid[nx][ny] = 2
                n_fresh -= 1
                new_q.append((nx, ny))

        q = new_q

    return mins if n_fresh == 0 else -1

def get_fresh_neighbors(grid, x, y):
    coords = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
    neighbors = []
    for coord_x, coord_y in coords:
        if not is_valid(grid, coord_x, coord_y):
            continue
        neighbors.append((coord_x, coord_y))
    return neighbors


def is_valid(grid, x, y):
    if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 1:
        return True
    return False


def test():
    grid = [[0, 1, 2],
            [1, 0, 0],
            [1, 1, 2]]

    assert oranges_rotting_v2(grid) == 3


def test_2():
    grid = [[1,2,1,1,2,1,1]]
    assert oranges_rotting_v2(grid) == 2