# Time: O(n)  Space: O(n)
def decode_ways(s):
    n = len(s)

    # dp[i] is the number of ways to decode the first i digits of s
    dp = [0] * (n + 1)

    # Base cases
    dp[0] = 1
    if s[0] != '0':
        dp[1] = 1

    for i in range(2, n + 1):
        option_1 = int(s[i - 1])
        option_2 = int(s[i - 2] + s[i - 1])
        option_1_ways, option_2_ways = 0, 0

        if 0 < option_1 < 10:
            option_1_ways = dp[i - 1]

        if 9 < option_2 < 27:
            option_2_ways = dp[i - 2]

        dp[i] = option_1_ways + option_2_ways

    return dp[-1]


def test():
    assert decode_ways(s='12') == 2
    assert decode_ways(s='226') == 3
    assert decode_ways(s='02') == 0