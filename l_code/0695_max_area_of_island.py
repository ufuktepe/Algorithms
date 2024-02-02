# Time: O(m*n)  Space: O(m*n) due to recursion
def max_area_of_island(grid):
    m, n = len(grid), len(grid[0])

    def visit(i, j):
        grid[i][j] = 0
        area = 1

        for x, y in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
            if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                area += visit(x, y)

        return area

    max_area = 0

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                area = visit(i, j)
                max_area = max(max_area, area)

    return max_area


def test():
    grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
    assert max_area_of_island(grid) == 6