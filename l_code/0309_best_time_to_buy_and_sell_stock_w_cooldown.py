# Tim: O(n)  Space: O(n)
def calc_profit(prices):
    n = len(prices)

    if n == 1:
        return 0

    # dp[i] is the max profit we can achieve up to day i
    dp = [0] * (n)

    # Base cases
    dp[0] = 0
    dp[1] = max(0, prices[1] - prices[0])

    best_profit = -1 * min(prices[0], prices[1])  # includes the last buy but doesn't include the last sell
    for i in range(2, n):
        dp[i] = max(prices[i] + best_profit, dp[i - 1])

        if best_profit < dp[i - 2] - prices[i]:
            best_profit = dp[i - 2] - prices[i]

    return dp[-1]


def test():
    prices = [1,2,3,0,2]
    assert calc_profit(prices) == 3


def test_2():
    prices = [1,2]
    assert calc_profit(prices) == 1


def test_3():
    prices = [6, 1, 4, 2, 3, 5]
    assert calc_profit(prices) == 5