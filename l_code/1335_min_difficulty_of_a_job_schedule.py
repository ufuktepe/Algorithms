# Let n be the num of jobs and d be the days
# Time: O(d*n^2)  Space: O(n*d)
def schedule(jobDifficulty, d):
    n = len(jobDifficulty)

    # dp[i][j] is the min difficulty using i days and the first j jobs
    # O(n*d)
    dp = [[float('inf')] * (n + 1) for _ in range(d + 1)]

    # Base case
    dp[0][0] = 0

    # O(d*n^2)
    for i in range(1, d + 1):
        for j in range(1, n + 1):
            min_difficulty = float('inf')
            cur_difficulty = 0
            for k in range(j, 0, -1):
                cur_difficulty = max(cur_difficulty, jobDifficulty[k-1])
                min_difficulty = min(min_difficulty, dp[i - 1][k - 1] + cur_difficulty)

            dp[i][j] = min_difficulty

    return dp[d][n] if dp[d][n] != float('inf') else -1


def test():
    jobDifficulty = [9, 9, 9]
    d = 4
    assert schedule(jobDifficulty, d) == -1


def test_2():
    jobDifficulty = [9, 9, 9]
    d = 3
    assert schedule(jobDifficulty, d) == 27


def test_3():
    jobDifficulty = [1, 2, 3]
    d = 2
    assert schedule(jobDifficulty, d) == 4


def test_4():
    jobDifficulty = [6, 5, 4, 3, 2, 1]
    d = 2
    assert schedule(jobDifficulty, d) == 7
