from collections import deque


# Time: O(N)  Space: O(N)
def shortest_path(grid):
    n = len(grid)
    if grid[0][0] != 0:
        return -1

    q = deque([(0, 0, 1)])

    while q:
        x, y, steps = q.popleft()

        if x == n - 1 and y == n - 1:
            return steps

        neighbors = get_neighbors(grid, x, y)

        for n_x, n_y in neighbors:
            q.append((n_x, n_y, steps + 1))
            grid[n_x][n_y] = -1

    return -1


def get_neighbors(grid, x, y):
    neighbors = []
    directions = [(x-1, y-1),
                  (x-1, y),
                  (x-1, y+1),
                  (x, y-1),
                  (x, y+1),
                  (x+1, y-1),
                  (x+1, y),
                  (x+1, y+1)]
    for a, b in directions:
        if is_valid(grid, a, b):
            neighbors.append((a, b))
    return neighbors


def is_valid(grid, x, y):
    if 0 <= x < len(grid) and 0 <= y < len(grid) and grid[x][y] == 0:
        return True
    return False


def test():
    grid = [[0, 0],
            [1, 0]]
    assert shortest_path(grid) == 2


def test_2():
    grid = [[0,1,1,0,0,0],
            [0,1,0,1,1,0],
            [0,1,1,0,1,0],
            [0,0,0,1,1,0],
            [1,1,1,1,1,0],
            [1,1,1,1,1,0]]
    assert shortest_path(grid) == 14