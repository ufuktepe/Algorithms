def is_interleave(s1, s2, s3):
    n = len(s1)
    m = len(s2)

    dp = [[False] * (m + 1) for i in range(n + 1)]

    # Base case
    dp[0][0] = True

    for i in range(n + 1):
        for j in range(m + 1):
            if i > 0 and s3[i + j - 1] == s1[i - 1]:
                dp[i][j] = dp[i - 1][j]
            if j > 0 and s3[i + j - 1] == s2[j - 1]:
                dp[i][j] = dp[i][j - 1] or dp[i][j]

    return dp[-1][-1]


def test():
    s1 = 'abc'
    s2 = 'de'
    s3 = 'abcde'
    assert is_interleave(s1, s2, s3)