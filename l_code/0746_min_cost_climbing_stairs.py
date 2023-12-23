def min_cost(cost):
    n = len(cost)

    # dp[i] is the min total cost to get to step i
    dp = [0 for i in range(n)]

    # Base cases
    dp[0] = cost[0]
    dp[1] = cost[1]

    for i in range(2, n):
        dp[i] = min(dp[i - 2], dp[i - 1]) + cost[i]

    return min(dp[-1], dp[-2])


def test():
    cost = [1, 5, 3, 1, 9, 2, 5, 1]
    assert min_cost(cost) == 7