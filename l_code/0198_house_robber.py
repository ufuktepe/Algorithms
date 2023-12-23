# Time: O(n)  Space: O(1)
def rob(nums):
    n = len(nums)
    if n == 1:
        return nums[0]
    # dp[i] is the max amount of money we can rob up to house at index i
    dp = [nums[0], max(nums[0], nums[1])]

    for i in range(2, n):
        prev = dp[1]
        dp[1] = max(dp[0] + nums[i], dp[1])
        dp[0] = prev

    return dp[-1]


def rob_memo(nums):
    memo = {}

    def dp(i):
        if i < 0:
            return 0
        if i not in memo:
            memo[i] = max(dp(i-1), dp(i-2) + nums[i])
        return memo[i]

    return dp(len(nums) - 1)


def test():
    nums = [1, 9, 11, 9, 4]
    assert rob_memo(nums) == 18
