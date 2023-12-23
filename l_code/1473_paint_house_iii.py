# Time: O(m*target*n)  Space: O(m*target*n)
def min_cost(cost, target, houses, m, n):
    dp = [[[float('inf')] * n for t in range(target + 1)] for _ in range(m + 1)]

    min_cost_colors = [[float('inf'), None] for t in range(target + 1)]
    next_min_cost_colors = [[float('inf'), None] for t in range(target + 1)]

    # Base cases
    min_cost_colors[0] = [0, None]
    next_min_cost_colors[0] = [0, None]

    for i in range(1, m + 1):
        temp_min_cost_colors = [[float('inf'), None] for t in range(target + 1)]
        temp_next_min_cost_colors = [[float('inf'), None] for t in range(target + 1)]
        for t in range(1, target + 1):
            for j in range(n):
                if houses[i - 1] != 0:
                    if j + 1 == houses[i - 1]:
                        if j == min_cost_colors[t - 1][1]:
                            dp[i][t][j] = min(dp[i - 1][t][j], next_min_cost_colors[t - 1][0])
                        else:
                            dp[i][t][j] = min(dp[i - 1][t][j], min_cost_colors[t - 1][0])
                else:
                    if j == min_cost_colors[t - 1][1]:
                        dp[i][t][j] = min(dp[i - 1][t][j], next_min_cost_colors[t - 1][0]) + cost[i - 1][j]
                    else:
                        dp[i][t][j] = min(dp[i - 1][t][j], min_cost_colors[t - 1][0]) + cost[i - 1][j]

                temp_min_cost_colors, temp_next_min_cost_colors = update_min_cost_colors(temp_min_cost_colors,
                                                                                         temp_next_min_cost_colors, t,
                                                                                         dp[i][t][j], j)

        min_cost_colors, next_min_cost_colors = temp_min_cost_colors, temp_next_min_cost_colors

    min_cost = min(dp[-1][-1])

    return min_cost if min_cost != float('inf') else -1


def update_min_cost_colors(min_cost_colors, next_min_cost_colors, t, cost, color):
    if min_cost_colors[t][0] > cost:
        next_min_cost_colors[t] = min_cost_colors[t]
        min_cost_colors[t] = [cost, color]
    elif next_min_cost_colors[t][0] > cost:
        next_min_cost_colors[t] = [cost, color]
    return min_cost_colors, next_min_cost_colors


def test():
    houses = [0,0,0,0,0]
    cost = [[1,10],[10,1],[10,1],[1,10],[5,1]]
    m = 5
    n = 2
    target = 3
    assert min_cost(cost, target, houses, m, n) == 9


def test_2():
    houses = [0, 2, 1, 2, 0]
    cost = [[1,10],[10,1],[10,1],[1,10],[5,1]]
    m = 5
    n = 2
    target = 3
    assert min_cost(cost, target, houses, m, n) == 11
