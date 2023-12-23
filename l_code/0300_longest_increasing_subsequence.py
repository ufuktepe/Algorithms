# Time: O(n^2)  Space: O(n)
def lis(nums):
    n = len(nums)

    # dp[i] is the length of the longest increasing subsequence ending at index i
    dp = [1] * n

    overall_max = 1
    # O(n^2)
    for i in range(1, n):
        max_length = 1
        for j in range(i):
            if nums[j] < nums[i]:
                max_length = max(max_length, dp[j] + 1)
        dp[i] = max_length
        overall_max = max(overall_max, max_length)

    return overall_max


def test():
    nums = [1]
    assert lis(nums) == 1


def test_2():
    nums = [1, 2]
    assert lis(nums) == 2


def test_3():
    nums = [2, 2]
    assert lis(nums) == 1


def test_4():
    nums = [2, 2, 5]
    assert lis(nums) == 2


def test_5():
    nums = [1, 6, 5, 16, 10, 29, 15, 20]
    assert lis(nums) == 5