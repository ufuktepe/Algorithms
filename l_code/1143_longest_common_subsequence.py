# Time: O(n*m)  Space: O(n*m)
def lcs(text1, text2):
    n = len(text1)
    m = len(text2)

    # dp[i][j] is the length of the lcs using the first i chars of text1 and j chars of text2
    dp = [[0 for j in range(m + 1)] for i in range(n + 1)]

    for i in range(1, n + 1):
        ch_1 = text1[i - 1]
        for j in range(1, m + 1):
            ch_2 = text2[j - 1]
            if ch_1 == ch_2:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[n][m]


def test():
    text1 = 'abcdef'
    text2 = 'xbyezf'
    assert lcs(text1, text2) == 3