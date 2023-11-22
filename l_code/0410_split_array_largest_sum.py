# Time: O(N^2*k)  Space: O(N*k)
def split_array(nums, k):
    # dp[i][j] is the min largest subarray sum considering the first j items with i subarrays
    dp = [[float('inf') for j in range(len(nums) + 1)] for i in range(k + 1)]

    # Base case: largest subarray sum is 0 if there are no subarrays and no items
    dp[0][0] = 0

    for i in range(1, k + 1):
        for j in range(1, len(nums) + 1):
            curr_sum = float('inf')
            running_sum = 0
            for q in range(j - 1, -1, -1):
                running_sum += nums[q]
                curr_sum = min(curr_sum, max(dp[i - 1][q], running_sum))
            dp[i][j] = curr_sum
    return dp[k][len(nums)]


def test_1():
    nums = [1, 2, 3, 4, 5]
    k = 2
    assert split_array(nums, k) == 9