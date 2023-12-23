def maximal_square(matrix):
    m = len(matrix)
    n = len(matrix[0])
    k = min(m, n)

    dp = [[[0 for j in range(n)] for i in range(m)] for a in range(k + 1)]

    max_area = 0
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == '1':
                max_area = 1
                dp[1][i][j] = 1
            else:
                dp[1][i][j] = 0

    for a in range(2, k + 1):
        for i in range(m - a + 1):
            for j in range(n - a + 1):
                if a % 2 == 0:
                    b = a // 2
                    if dp[b][i][j] and dp[b][i][j + b] and dp[b][i + b][j + b] and dp[b][i + b][j]:
                        dp[a][i][j] = 1
                    else:
                        dp[a][i][j] = 0
                else:
                    b = a // 2 + 1
                    if dp[b][i][j] and dp[b][i][j + b - 1] and dp[b][i + b - 1][j + b - 1] and dp[b][i + b - 1][j]:
                        dp[a][i][j] = 1
                    else:
                        dp[a][i][j] = 0

                if dp[a][i][j] == 1:
                    max_area = a ** 2

    return max_area


def test():
    matrix = [['1', '0'], ['1', '1']]
    assert maximal_square(matrix) == 1


def test_2():
    matrix = [["1","0","1","0","0"],
              ["1","0","1","1","1"],
              ["1","1","1","1","1"],
              ["1","0","0","1","0"]]
    assert maximal_square(matrix) == 4