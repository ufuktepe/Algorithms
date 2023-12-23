def calc_profit(prices, fee):
    n = len(prices)

    # dp[i] is the max profit we can achieve up to day i
    dp = [0] * n

    best_profit = -prices[0]

    for i in range(1, n):
        dp[i] = max(prices[i] + best_profit - fee, dp[i - 1])
        best_profit = max(best_profit, dp[i - 1] - prices[i])

    return dp[-1]


def test():
    prices = [1, 3, 2, 8, 4, 9]
    fee = 2
    assert calc_profit(prices, fee) == 8