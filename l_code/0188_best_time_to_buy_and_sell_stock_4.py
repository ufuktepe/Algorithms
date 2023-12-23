def max_profit(prices, k):
    n = len(prices)

    # dp[i][j] is the max profit we can get at the end of day j by performing at most i transactions
    dp = [[0] * (n + 1) for _ in range(k + 1)]

    for i in range(1, k + 1):
        max_diff = -prices[0]
        for j in range(1, n + 1):
            profit_1 = dp[i][j-1]               # We don't buy or sell
            profit_2 = max_diff + prices[j-1]   # We sell on this day
            dp[i][j] = max(profit_1, profit_2)

            # Update max_diff
            if dp[i-1][j-1] - prices[j-1] > max_diff:
                max_diff = dp[i-1][j-1] - prices[j-1]

    return dp[-1][-1]



def test():
    k = 1
    prices = [1, 2, 3, 4, 3, 2, 1]
    assert max_profit(prices, k) == 3


def test_2():
    k = 2
    prices = [2, 4, 1]
    assert max_profit(prices, k) == 2


def test_3():
    k = 2
    prices = [3, 2, 6, 5, 0, 3]
    assert max_profit(prices, k) == 7