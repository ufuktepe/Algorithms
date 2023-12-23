# Time: O(N)  Space: O(N)
def max_subarray(nums):
    # dp[i] is the subarray with the largest sum that ends at index i of nums
    dp = [0] * len(nums)  # O(N)

    # Base case
    dp[0] = nums[0]

    max_sum = nums[0]
    # O(N)
    for i in range(1, len(nums)):
        dp[i] = max(dp[i - 1] + nums[i], nums[i])
        max_sum = max(max_sum, dp[i])

    return max_sum


# Time: O(N)  Space: O(1)
def max_subarray_opt(nums):
    cur_max = nums[0]

    max_sum = nums[0]
    # O(N)
    for i in range(1, len(nums)):
        cur_max = max(cur_max + nums[i], nums[i])
        max_sum = max(max_sum, cur_max)

    return max_sum


def test():
    nums = [2, 4, 6, -2, 10, -5]
    assert max_subarray_opt(nums) == 20


def test_2():
    nums = [-1]
    assert max_subarray_opt(nums) == -1