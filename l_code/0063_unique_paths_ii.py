# Time: O(n*m)  Space: O(n*m)
def unique_paths(grid):
    if grid[0][0] == 1:
        return 0

    m = len(grid)
    n = len(grid[0])

    # dp[i][j] is the number of unique paths to reach grid[i-1][j-1] from grid[0][0]
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Base case
    dp[1][1] = 1

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if (i == 1 and j == 1) or grid[i - 1][j - 1]:
                continue
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    return dp[m][n]


# Time: O(n*m)  Space: O(1)
def unique_paths_opt(grid):
    if grid[0][0] == 1:
        return 0

    m = len(grid)
    n = len(grid[0])

    # Base cases
    grid[0][0] = 1

    for i in range(m):
        for j in range(n):
            if i == 0 and j == 0:
                continue

            if grid[i][j] == 1:
                grid[i][j] = 0
            else:
                if i > 0:
                    grid[i][j] += grid[i - 1][j]
                if j > 0:
                    grid[i][j] += grid[i][j - 1]

    return grid[-1][-1]


def test():
    grid = [[0, 0, 0],
            [0, 1, 0],
            [0, 0, 0]]
    assert unique_paths_opt(grid) == 2