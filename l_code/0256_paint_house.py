# Time: O(n) Space: O(n)
def min_cost(costs):
    n = len(costs)

    # dp[i][j] is the min cost of painting first j houses where the jth house is color i
    dp = [[float('inf')] * (n + 1) for _ in range(3)]

    dp[0][0] = dp[1][0] = dp[2][0] = 0

    for j in range(1, n + 1):
        for i in range(3):
            dp[i][j] = min(dp[(i + 1) % 3][j - 1], dp[(i + 2) % 3][j - 1]) + costs[j - 1][i]

    return min(dp[0][-1], dp[1][-1], dp[2][-1])


def test():
    costs = [[17,2,17],[16,16,5],[14,3,19]]
    assert min_cost(costs) == 10