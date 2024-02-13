import heapq
from functools import lru_cache


def max_profit(startTime, endTime, profit):
    n = len(startTime)
    jobs = []  # (startTime, endTime, profit)
    for i in range(n):
        jobs.append((startTime[i], endTime[i], profit[i]))
    jobs.sort(key=lambda item: item[1])

    # dp[i] is the max profit we can get using the first i jobs
    dp = [0] * (n + 1)

    for idx in range(1, n + 1):
        i = idx - 1
        j = get_non_conflicting_index(i, jobs)
        if j is None:
            dp[idx] = max(dp[idx - 1], jobs[i][2])
        else:
            dp[idx] = max(dp[idx - 1], dp[j + 1] + jobs[i][2])

    return dp[-1]

def get_non_conflicting_index(i, jobs):
    left, right = 0, i - 1
    start_time = jobs[i][0]

    while left <= right:
        mid = (left + right) // 2

        if jobs[mid][1] <= start_time:
            left = mid + 1
        else:
            right = mid - 1

    return right if right >= 0 else None

def max_profit_rec(startTime, endTime, profit):
    # cache = {}
    n = len(startTime)
    jobs = []  # (startTime, endTime, profit)
    for i in range(n):
        jobs.append((startTime[i], endTime[i], profit[i]))
    jobs.sort()

    def get_next_non_conflicting_index(i, jobs):
        end_time = jobs[i][1]
        left = i + 1
        right = len(jobs) - 1

        while left <= right:
            mid = (left + right) // 2

            if jobs[mid][0] < end_time:
                left = mid + 1
            elif jobs[mid][0] >= end_time:
                right = mid - 1

        return left if left < len(jobs) else None

    @lru_cache
    def dfs(i):
        if i == n:
            return 0

        # if i in cache:
        #     return cache[i]

        # don't include
        res1 = dfs(i + 1)

        # include
        j = get_next_non_conflicting_index(i, jobs)
        if j is not None:
            res2 = dfs(j) + jobs[i][2]
        else:
            res2 = jobs[i][2]

        return max(res1, res2)

        # return cache[i]

    return dfs(0)

def max_profit_sweep_line(startTime, endTime, profit):
    n = len(startTime)
    events = []
    for i in range(n):
        # 1 for start event
        # 0 for end event
        # We want end events to occur before start event for same time
        events.append((startTime[i], 1, i))
        events.append((endTime[i], 0, i))

    events.sort()

    # dp[i] is the max profit we can get at the start time of the ith job
    dp = [0] * n
    max_so_far = 0

    for time, event_type, index in events:
        if event_type == 1:
            # Starting time of job[index]
            dp[index] = max_so_far
        else:
            # End time of job[index]
            max_so_far = max(dp[index] + profit[index], max_so_far)

    return max_so_far

def test():
    startTime = [4,3,1,2,4,8,3,3,3,9]
    endTime = [5,6,3,5,9,9,8,5,7,10]
    profit = [9,9,5,12,10,11,10,4,14,7]
    assert max_profit_sweep_line(startTime, endTime, profit) == 37
