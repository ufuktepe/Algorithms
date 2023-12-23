from collections import defaultdict


# Time: O(N*log(N))  Space: O(N)
def delete_and_earn(nums):
    vals = defaultdict(int)

    # O(N)
    for num in nums:
        vals[num] += num

    # O(N)
    numbers = [i for i in vals]

    # O(N*log(N))
    numbers.sort()

    dp = [0 for i in range(len(numbers) + 1)]

    # Base case
    dp[1] = vals[numbers[0]]

    # O(N)
    for i in range(2, len(numbers) + 1):
        prev_num = numbers[i - 2]
        cur_num = numbers[i - 1]

        if cur_num - prev_num == 1:
            dp[i] = max(dp[i - 2] + vals[cur_num], dp[i - 1])
        else:
            dp[i] = dp[i - 1] + vals[cur_num]

    return dp[-1]



# Time: O(N*log(N))  Space: O(N)
def delete_and_earn(nums):
    vals = defaultdict(int)
    max_num = 0

    # O(N)
    for num in nums:
        vals[num] += num
        max_num = max(max_num, num)

    dp = [0 for i in range(max_num + 1)]

    # Base case
    dp[1] = vals[1]

    # O(N)
    for i in range(2, max_num + 1):
        dp[i] = max(dp[i - 2] + vals[i], dp[i - 1])

    return dp[-1]


def test():
    nums = [1, 3, 5, 3, 1]
    assert delete_and_earn(nums) == 13

    nums = [2, 2, 3, 3, 3, 4]
    assert delete_and_earn(nums) == 9


