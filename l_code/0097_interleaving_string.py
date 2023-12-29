# Let n, m, k be the lengths of s1, s2, s3 respectively
# Time: O(n, m, k)  Space: O(n, m, k)
def is_interleave(s1, s2, s3):
    n1, n2, n3 = len(s1), len(s2), len(s3)

    # dp[i][j][k] is whether s3[:i] can be formed by interleaving s1[:j] and s2[:k]
    dp = [[[False] * (n2 + 1) for j in range(n1 + 1)] for i in range(n3 + 1)]

    # Base case
    dp[0][0][0] = True

    for i in range(1, n3 + 1):
        for j in range(n1 + 1):
            for k in range(n2 + 1):
                opt1, opt2 = False, False
                if j > 0 and s3[i - 1] == s1[j - 1]:
                    opt1 = dp[i - 1][j - 1][k]
                if k > 0 and s3[i - 1] == s2[k - 1]:
                    opt2 = dp[i - 1][j][k - 1]

                dp[i][j][k] = opt1 or opt2

    return dp[-1][-1][-1]


def is_interleave_opt(s1, s2, s3):
    n1, n2, n3 = len(s1), len(s2), len(s3)

    # dp[i] is whether s3 can be formed by interleaving s1[:len(s3) - k] and s2[:k]
    dp = [False] * (n2 + 1)

    # Base case
    dp[0] = True

    for i in range(1, n3 + 1):
        for j in range(n1 + 1):
            for k in range(n2 + 1):
                opt1, opt2 = False, False
                if j > 0 and s3[i - 1] == s1[j - 1]:
                    # opt1 = dp[i - 1][j - 1][k]
                    opt1 = dp[k]
                if k > 0 and s3[i - 1] == s2[k - 1]:
                    # opt2 = dp[i - 1][j][k - 1]
                    opt2 = dp[k - 1]

                dp[k] = opt1 or opt2

            dp_prev_j = dp_j
            dp_j = dp

    return dp[-1]


def test():
    s1 = 'ac'
    s2 = 'b'
    s3 = 'abc'
    assert is_interleave_opt(s1, s2, s3) == True


def test_2():
    s1 = 'ac'
    s2 = 'ba'
    s3 = 'abc'
    assert is_interleave_opt(s1, s2, s3) == False


def test_3():
    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbcbcac"
    assert is_interleave_opt(s1, s2, s3) == True


def test_4():
    s1 = ""
    s2 = ""
    s3 = ""
    assert is_interleave_opt(s1, s2, s3) == True


