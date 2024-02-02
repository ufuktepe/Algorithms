# Time: O(n*m)  Space: O(n*m)
def is_match(s, p):
    n = len(s)
    m = len(p)

    # dp[i][j] indicates whether s[:i+1] and p[:j+1] match
    dp = [[False] * (m + 1) for _ in range(n + 1)]

    # Base cases
    dp[0][0] = True

    for j in range(1, m + 1):
        if p[j-1] == '*':
            dp[0][j] = True
        else:
            break

    for i in range(1, n + 1):
        cur_s = s[i - 1]
        for j in range(1, m + 1):
            cur_p = p[j - 1]

            if cur_p == '?' or cur_p == cur_s:
                dp[i][j] = dp[i - 1][j - 1]
            elif cur_p == '*':
                dp[i][j] = dp[i][j - 1] or dp[i - 1][j]

    return dp[-1][-1]


def test():
    assert is_match(s='abc', p='ab?')
    assert is_match(s='abc', p='ab*')
    assert is_match(s='abc', p='a?c')
    assert is_match(s='abc', p='*')
    assert is_match(s='abc', p='*c')
    assert is_match(s='abc', p='*bc')
    assert is_match(s='abc', p='*abc')
    assert is_match(s='abc', p='*?c')
    assert is_match(s='abcd', p='?*d')
    assert is_match(s='abcd', p='?*c') is False