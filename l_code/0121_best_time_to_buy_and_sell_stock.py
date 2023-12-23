# Time: O(n)  Space: O(1)
def calc_profit(prices):
    n = len(prices)
    if n == 1:
        return 0

    max_profit = 0
    min_so_far = prices[0]

    for i in range(1, n):
        max_profit = max(max_profit, prices[i] - min_so_far)
        if min_so_far > prices[i]:
            min_so_far = prices[i]

    return max_profit


def test():
    prices = [1, 2, 3, 4, 5, 3, 1]
    assert calc_profit(prices) == 4