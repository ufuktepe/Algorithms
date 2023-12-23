# Time: O(n)  Space: O(n)
def calc_profit(prices):
    n = len(prices)

    dp = [[0] * (n + 1) for _ in range(3)]

    for t in range(1, 3):
        max_diff = -prices[0]
        for i in range(1, n + 1):
            dp[t][i] = max(dp[t][i - 1], max_diff + prices[i - 1])
            max_diff = max(max_diff, dp[t - 1][i] - prices[i - 1])

    return dp[-1][-1]


def test():
    prices = [3, 3, 5, 0, 0, 3, 1, 4]
    assert calc_profit(prices) == 6


def test_2():
    prices = [7,6,4,3,1]
    assert calc_profit(prices) == 0