# Time: O(n)  Space: O(n)
def num_tilings(n):
    C = 10 ** 9 + 7

    if n == 1:
        return 1

    # dp[i] is the num of ways to tile a 2 x i tile where all tiles are covered
    dp = [0] * (n + 1)

    # dp_top[i] is the num of ways to tile a 2 x i tile where the top right is empty
    dp_top = [0] * (n + 1)

    # dp_bot[i] is the num of ways to tile a 2 x i tile where the bottom right is empty
    dp_bot = [0] * (n + 1)

    # base cases
    dp[1] = 1
    dp[2] = 2
    dp_top[2] = 1
    dp_bot[2] = 1

    for i in range(3, n + 1):
        dp[i] = (dp[i - 1] + dp_top[i - 1] + dp_bot[i - 1] + dp[i - 2]) % C
        dp_top[i] = (dp_bot[i - 1] + dp[i - 2]) % C
        dp_bot[i] = (dp_top[i - 1] + dp[i - 2]) % C

    return dp[n]


def test():
    assert num_tilings(1) == 1
    assert num_tilings(2) == 2
    assert num_tilings(3) == 5