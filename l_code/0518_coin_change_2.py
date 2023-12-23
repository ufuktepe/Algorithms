# Time: O(n*amount)  Space: O(n*amount)
def coin_change(coins, amount):
    # dp[i][j] is the num of ways that make up amount j using the first i coins
    dp = [[0] * (amount + 1) for _ in range(len(coins) + 1)]

    # Base cases - we can get amount 0 with any coins
    for i in range(len(coins) + 1):
        dp[i][0] = 1

    for i in range(1, len(coins) + 1):
        cur_coin = coins[i - 1]
        for j in range(1, amount + 1):
            if j - cur_coin >= 0:
                dp[i][j] = dp[i - 1][j] + dp[i][j - cur_coin]
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[-1][-1]


# Time: O(n*amount)  Space: O(amount)
def coin_change_opt(coins, amount):
    # dp[i] is the num of ways that make up amount j
    dp = [0] * (amount + 1)

    # Base case - we can get amount 0
    dp[0] = 1

    for cur_coin in coins:
        for j in range(1, amount + 1):
            if j - cur_coin >= 0:
                dp[j] = dp[j] + dp[j - cur_coin]

    return dp[-1]


def test():
    amount = 3
    coins = [2]
    assert coin_change_opt(coins, amount) == 0


def test_2():
    amount = 10
    coins = [10]
    assert coin_change_opt(coins, amount) == 1