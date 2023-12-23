# Time: O(m*n)  Space: O(m*n)
def num_ways(m, n):
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Base case
    dp[1][1] = 1

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if i == 1 and j == 1:
                continue
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    return dp[m][n]


def num_ways_rec(m, n):
    if m == 1 and n == 1:
        return 1
    if m == 0 or n == 0:
        return 0

    return num_ways_rec(m - 1, n) + num_ways_rec(m, n - 1)



def test():
    m = 3
    n = 7
    assert num_ways_rec(m, n) == 28