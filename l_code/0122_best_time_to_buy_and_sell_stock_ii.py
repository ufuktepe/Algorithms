# Time: O(n)  Space: O(n)
def calc_profit(prices):
    n = len(prices)

    # dp[i] is the total max profit we can get up to day i
    dp = [0] * n

    max_diff_so_far = -prices[0]
    for i in range(1, n):
        dp[i] = max(dp[i - 1], prices[i] + max_diff_so_far)

        if max_diff_so_far < dp[i - 1] - prices[i]:
            max_diff_so_far = dp[i - 1] - prices[i]

    return dp[-1]


def test():
    prices = [3, 1, 6, 4, 5, 3]
    assert calc_profit(prices) == 6


def test_2():
    prices = [3]
    assert calc_profit(prices) == 0


def test_3():
    prices = [3, 1]
    assert calc_profit(prices) == 0


def test_4():
    prices = [3, 4]
    assert calc_profit(prices) == 1