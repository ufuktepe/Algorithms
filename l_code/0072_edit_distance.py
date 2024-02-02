# Time: O(m*n)  Space: O(m*n)
def edit_distance(word1, word2):
    m = len(word1)
    n = len(word2)

    # dp[i][j] is the min num of operations to convert word1[:i+1] to word2[:j+1]
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Base cases
    for j in range(n + 1):
        dp[0][j] = j
    for i in range(m + 1):
        dp[i][0] = i

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1]) + 1

    return dp[-1][-1]


def test():
    assert edit_distance(word1='abc', word2='ab') == 1
    assert edit_distance(word1='ac', word2='abc') == 1
    assert edit_distance(word1='ac', word2='ad') == 1
    assert edit_distance(word1='', word2='ad') == 2
    assert edit_distance(word1='ac', word2='') == 2
    assert edit_distance(word1='rbd', word2='abcd') == 2
