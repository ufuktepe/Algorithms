from collections import deque


def longest_ones(nums, k):
    n = len(nums)
    max_ones = 0

    q = deque()
    i, j = 0, 0

    cur = 0
    while j < n:
        if nums[j] == 0:
            cur += 1
            q.append(j)
        else:
            cur += 1

        if len(q) == k + 1:
            oldest_index = q.popleft()  # index of the oldest 0
            cur -= (oldest_index - i + 1)
            i = oldest_index + 1

        j += 1
        max_ones = max(max_ones, cur)

    return max_ones


def test():
    nums = [1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1]
    assert longest_ones(nums, 2) == 9