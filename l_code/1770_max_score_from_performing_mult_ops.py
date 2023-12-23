def max_score(nums, multipliers):
    n = len(nums)
    m = len(multipliers)

    # dp[i][j] is the max score using the first i and last j numbers
    dp = [[0 for j in range(m + 1)] for i in range(m + 1)]
    max_score = float('-inf')

    for k, multiplier in enumerate(multipliers):
        n_multipliers = k + 1
        for i in range(n_multipliers + 1):
            j = n_multipliers - i

            left_score = dp[i - 1][j] + multiplier * nums[i - 1] if i > 0 else float('-inf')
            right_score = dp[i][j - 1] + multiplier * nums[n - j] if j > 0 else float('-inf')

            dp[i][j] = max(left_score, right_score)
            if n_multipliers == m:
                max_score = max(max_score, dp[i][j])

    return max_score


def test():
    nums = [-5,-3,-3,-2,7,1]
    multipliers = [-10,-5,3,4,6]
    assert max_score(nums, multipliers) == 102