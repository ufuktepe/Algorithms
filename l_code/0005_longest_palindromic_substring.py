# Time: O(n^2)  Space: O(n^2)
def longestPalindrome(s):
    n = len(s)
    # dp[i][j] indicates whether s[i:j+1] is a palindrome
    dp = [[False] * n for _ in range(n + 1)]

    # Base cases
    for i in range(n):
        dp[i][i] = True      # length 1
        dp[i + 1][i] = True  # length 0

    start = 0
    end = 1
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = dp[i + 1][j - 1] and s[i] == s[j]
            if dp[i][j]:
                start = i
                end = j + 1
    return s[start:end]


def test():
    assert longestPalindrome('bb') == 'bb'
    assert longestPalindrome('bba') == 'bb'
    assert longestPalindrome('abba') == 'abba'
    assert longestPalindrome('xyzabbax') == 'abba'