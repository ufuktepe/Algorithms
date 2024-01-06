def is_match2(s, p):
    def get_chars(i):
        if i >= len(p):
            return None, None

        if p[i] == '*':
            nxt = p[i + 1] if i + 1 < len(p) else None
            prev = p[i - 1] if i - 1 >= 0 else None

            return prev, nxt

        return None, None

    def _is_match(s, p, i):
        prev, nxt = get_chars(i)

        for ch in s:
            if i >= len(p):
                return False

            if p[i] == '.' or ch == p[i]:
                i += 1
                prev, nxt = get_chars(i)

            elif p[i] == '*':
                if ch == prev or prev == '.':
                    pass
                elif ch == nxt or nxt == '.':
                    i += 2
                    prev, nxt = get_chars(i)
                else:
                    return False
            else:
                return False

        return True

    for i in range(len(p)):
        if _is_match(s, p, i):
            return True

    return False


def is_match(s, p):
    n = len(s)
    m = len(p)

    # dp[i][j] indicates whether the first i chars of s matches up with the first j chars of p
    dp = [[False] * (m + 1) for _ in range(n + 1)]

    # Base case
    dp[0][0] = True

    # Base cases: deal with patterns like a*  or a*b* or a*b*c* etc.
    for j in range(2, m + 1):
        p_ch = p[j - 1]
        if p_ch == '*':
            dp[0][j] = dp[0][j - 2]

    for i in range(1, n + 1):
        s_ch = s[i - 1]
        for j in range(1, m + 1):
            p_ch = p[j - 1]

            if p_ch == '.' or p_ch == s_ch:
                dp[i][j] = dp[i - 1][j - 1]
            elif p_ch == '*':
                if dp[i][j - 2]:
                    dp[i][j] = dp[i][j - 2]  # match 0 occurances of p[j - 2]
                elif p[j - 2] == s_ch or p[j - 2] == '.':
                    dp[i][j] = dp[i - 1][j - 1]

    return dp[-1][-1]


def test():
    s = 'b'
    p = 'a*b'
    assert is_match(s, p)



# def test():
#     s = 'aab'
#     p = 'c*a*b'
#     assert is_match(s, p)
#
#
# def test_2():
#     s = 'aa'
#     p = 'a'
#     assert is_match(s, p) is False
#
#
# def test_3():
#     s = 'abcde'
#     p = 'a.*de'
#     assert is_match(s, p)