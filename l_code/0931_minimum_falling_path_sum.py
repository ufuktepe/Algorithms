# Time: O(n*n)  Space: O(n*n)
def min_falling_path(matrix):
    n = len(matrix)

    # dp[i][j] is the min falling path from first row to matrix[i][j - 1]
    dp = [[float('inf')] * (n + 2) for _ in range(n)]

    # Base cases
    for j in range(1, n + 1):
        dp[0][j] = matrix[0][j - 1]

    for i in range(1, n):
        for j in range(1, n + 1):
            dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i - 1][j + 1]) + matrix[i][j - 1]

    return min(dp[-1])


def test():
    matrix = [[2,1,3],[6,5,4],[7,8,9]]
    assert min_falling_path(matrix) == 13