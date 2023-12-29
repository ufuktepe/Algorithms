def num_of_rolls(n, k, target):
    # dp[i][j]  num of ways to reach j using i dice
    # dp[i][j] = dp[i - 1][j - target]
    dp = [[0] * (target + 1) for _ in range(n + 1)]

    # Base case
    dp[0][0] = 1

    for i in range(1, n + 1):
        for j in range(target + 1):
            for m in range(k + 1):
                if j >= m:
                    dp[i][j] = (dp[i][j] + dp[i - 1][j - m])  % (10 ** 9 + 7)
    return dp


print(num_of_rolls(n=2, k=6, target=7))