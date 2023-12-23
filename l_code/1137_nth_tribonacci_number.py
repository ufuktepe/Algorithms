# Time: O(N)  Space: O(N)
def tribonacci(n):
    dp = [None for i in range(max(n + 1, 3))]

    # Base cases
    dp[0] = 0
    dp[1] = 1
    dp[2] = 1

    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

    return dp[n]


def tribonacci_constant_space(n):
    dp = [0, 1, 1]
    if n < 3:
        return dp[n]

    for i in range(3, n + 1):
        temp_1 = dp[1]
        temp_2 = dp[2]
        dp[2] = dp[2] + dp[1] + dp[0]
        dp[0] = temp_1
        dp[1] = temp_2

    return dp[-1]


def test():
    assert tribonacci(0) == 0
    assert tribonacci(2) == 1
    assert tribonacci(4) == 4
    assert tribonacci(11) == 274