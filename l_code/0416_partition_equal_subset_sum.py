def can_partition(nums):
    total = sum(nums)
    if total % 2 != 0:
        return False

    target = total // 2
    n = len(nums)

    # dp[i][j] indicates whether we can create a subset from the first i items in nums that sums to j
    dp = [[False] * (target + 1) for _ in range(n + 1)]

    # Base case
    dp[0][0] = True

    for i in range(1, n + 1):
        for j in range(target + 1):
            if j - nums[i - 1] >= 0:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[-1][-1]

