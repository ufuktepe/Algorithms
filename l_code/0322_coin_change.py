# Let N be the number of coins and M be the amount
# Time: O(N*M)  Space: O(N)
def coin_change(coins, amount):
    # dp[i] is the minimum number of coins required to make amount i
    dp = [float('inf') for i in range(amount + 1)]
    dp[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i-coin] + 1)

    return dp[amount] if dp[amount] < float('inf') else -1


def test():
    coins = [1, 2, 5]
    amount = 9
    assert coin_change(coins, amount) == 3


def test_2():
    coins = [3, 5]
    amount = 7
    assert coin_change(coins, amount) == -1
