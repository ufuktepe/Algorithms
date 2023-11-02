# 2-D DP (reduced to 0-1 knapsack problem)
def find_target_sum_ways(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    if len(nums) == 0:
        return 0

    sum_nums = sum(nums)
    if (sum_nums + target) % 2 != 0 or sum_nums < abs(target):
        return 0

    w = int((sum_nums + target) / 2)
    n = len(nums)

    # dp[i][j] represents the number of subsets that sum up to j using the first i items in nums
    dp = [[0 for j in range(w + 1)] for i in range(n + 1)]

    # Base case: there is one way to form a subset that sums to 0 using an empty set
    dp[0][0] = 1
    # for i in range(n + 1):
    #     dp[i][0] = 1

    for i in range(1, n + 1):
        curr_num = nums[i - 1]
        for j in range(w + 1):
            if j >= curr_num:
                # dp[i - 1][j]            -> exclude curr_num
                # dp[i - 1][j - curr_num] -> include curr_num
                dp[i][j] = dp[i - 1][j] + dp[i - 1][j - curr_num]
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[n][w]


# 1-D DP (reduced to 0-1 knapsack problem)
def find_target_sum_ways_v2(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    if len(nums) == 0:
        return 0

    sum_nums = sum(nums)
    if (sum_nums + target) % 2 != 0 or sum_nums < abs(target):
        return 0

    w = int((sum_nums + target) / 2)

    # dp[j] represents the number of subsets that sum up to j
    dp = [0 for j in range(w + 1)]

    # Base case: there is one way to form a subset that sums to 0
    dp[0] = 1

    for num in nums:
        for j in range(w, -1, -1):
            if j >= num:
                dp[j] += dp[j - num]

    return dp[-1]


# 1-D DP solution
def find_target_sum_ways_v3(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    if len(nums) == 0:
        return 0
    sum_nums = sum(nums)

    if abs(target) > sum_nums:
        return 0

    # dp[sum_nums + j] represents the number of subsets that sum up to j
    dp = [0 for _ in range(2 * sum_nums + 1)]

    # Base case
    dp[sum_nums] = 1

    for num in nums:
        nxt = [0 for _ in range(2 * sum_nums + 1)]
        for j in range(2 * sum_nums + 1):
            if j - num >= 0:
                # Up to now, there are dp[j] subsets that sum to (j - sum_nums).
                # We can add -num to each set, so each set sums to (j - sum_nums - num).
                nxt[j - num] += dp[j]

            if j + num <= 2 * sum_nums:
                # Up to now, there are dp[j] subsets that sum to (j - sum_nums).
                # We can add +num to each set, so each set sums to (j - sum_nums + num).
                nxt[j + num] += dp[j]
        dp = nxt

    return dp[target + sum_nums]


def test_1():
    nums = [1, 1, 1, 1, 1]
    target = 3
    assert find_target_sum_ways_v3(nums, target) == 5
