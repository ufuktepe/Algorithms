
# Time: O(n*k)  Space: O(n*k)
def min_cost(costs):
    n = len(costs)
    k = len(costs[0])

    # dp[i][j] is the min cost to paint the first i+1 houses where the last house is painted in color j
    dp = [[0] * k for _ in range(n)]

    min_cost_color = [float('inf'), None]
    next_min_cost_color = [float('inf'), None]

    # Base cases
    for j in range(k):
        dp[0][j] = costs[0][j]
        min_cost_color, next_min_cost_color = update_min_cost_color(min_cost_color, next_min_cost_color, costs[0][j], j)

    for i in range(1, n):
        temp_min_cost_color = [float('inf'), None]
        temp_next_min_cost_color = [float('inf'), None]
        for j in range(k):
            if min_cost_color[1] != j:
                dp[i][j] = min_cost_color[0] + costs[i][j]
            else:
                dp[i][j] = next_min_cost_color[0] + costs[i][j]

            temp_min_cost_color, temp_next_min_cost_color = update_min_cost_color(temp_min_cost_color,
                                                                                  temp_next_min_cost_color,
                                                                                  dp[i][j],
                                                                                  j)
        min_cost_color, next_min_cost_color = temp_min_cost_color, temp_next_min_cost_color

    return min(dp[-1])


def update_min_cost_color(min_cost_color, next_min_cost_color, cost, color):
    if min_cost_color[0] > cost:
        next_min_cost_color = min_cost_color
        min_cost_color = [cost, color]
    elif next_min_cost_color[0] > cost:
        next_min_cost_color = [cost, color]
    return min_cost_color, next_min_cost_color


def test():
    costs = [[1,5,3],[2,9,4]]
    assert min_cost(costs) == 5


def test_2():
    costs = [[1,3],[2,4]]
    assert min_cost(costs) == 5