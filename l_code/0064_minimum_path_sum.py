import heapq


# Time: O(m*n*log(m*n))  Space: O(m*n)
def min_path_sum(grid):
    m = len(grid)
    n = len(grid[0])

    min_dist = [[float('inf')] * n for _ in range(m)]

    min_dist[0][0] = grid[0][0]

    pq = [(grid[0][0], 0, 0)]  # min_dist, x, y

    # O(m*n*log(m*n))
    while pq:
        dist, x, y = heapq.heappop(pq)  # O(log(m*n))

        for n_x, n_y in get_adj(grid, x, y):
            n_dist = min_dist[n_x][n_y]

            if n_dist > dist + grid[n_x][n_y]:
                n_dist = dist + grid[n_x][n_y]
                min_dist[n_x][n_y] = n_dist
                heapq.heappush(pq, (n_dist, n_x, n_y))  # O(log(m*n))

    return min_dist[-1][-1]


def get_adj(grid, x, y):
    adj = []
    if x + 1 < len(grid):
        adj.append((x + 1, y))
    if y + 1 < len(grid[0]):
        adj.append((x, y + 1))
    return adj


# Time: O(m*n)  Space: O(m*n)
def min_path_sum_dp(grid):
    m = len(grid)
    n = len(grid[0])

    # dp[i][j] is the min path sum to get to grid[i][j] from grid[0][0]
    dp = [[float('inf')] * n for _ in range(m)]

    # Base case
    dp[0][0] = grid[0][0]

    for i in range(m):
        for j in range(n):
            if i > 0:
                dp[i][j] = dp[i - 1][j] + grid[i][j]
            if j > 0:
                dp[i][j] = min(dp[i][j], dp[i][j - 1] + grid[i][j])
    return dp[-1][-1]


def test():
    grid = [[1,3,1],[1,5,1],[4,2,1]]
    assert min_path_sum_dp(grid) == 7