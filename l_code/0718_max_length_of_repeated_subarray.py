# Time: O(m*n)  Space: O(m*n)
def max_len_subarray(nums1, nums2):
    n = len(nums1)
    m = len(nums2)

    # dp[i][j] is the max length of subarray that ends at nums1[i - 1] and nums2[j - 1]
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    max_len = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if nums1[i - 1] == nums2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                max_len = max(max_len, dp[i][j])
            else:
                dp[i][j] = 0

    return max_len


def test_1():
    nums1 = [1, 2, 3]
    nums2 = [2, 3]
    assert max_len_subarray(nums1, nums2) == 2


def test_2():
    nums1 = [1, 2, 3]
    nums2 = [2, 4]
    assert max_len_subarray(nums1, nums2) == 1


def test_3():
    nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    nums2 = [9, 5, 6, 7, 8, 9, 1, 2, 3]
    assert max_len_subarray(nums1, nums2) == 5