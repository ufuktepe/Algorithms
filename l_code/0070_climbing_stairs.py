def memoize(f):
    cache = {}

    def wrapper(*args):
        n = args[1]

        if n in cache:
            return cache[n]

        cache[n] = f(*args)
        return cache[n]

    return wrapper


class Solution:
    @memoize
    def climbStairs(self, n):
        if n < 3:
            return n

        return self.climbStairs(n - 1) + self.climbStairs(n - 2)


def climb_stairs_rec(n):
    cache = {1: 1, 2: 2}

    def compute(n):
        if n in cache:
            return cache[n]

        cache[n] = compute(n - 1) + compute(n - 2)
        return cache[n]

    return compute(n)


def climb_stairs_iter(n):
    if n < 3:
        return n

    # dp[i] represents the number of ways you can climb i stairs
    dp = [None for _ in range(n + 1)]

    # Base cases
    dp[0] = 0
    dp[1] = 1
    dp[2] = 2

    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]

def test_decorator():
    solution = Solution()
    assert solution.climbStairs(1) == 1
    assert solution.climbStairs(2) == 2
    assert solution.climbStairs(3) == 3
    assert solution.climbStairs(4) == 5


def test_climb_stairs_rec():
    assert climb_stairs_rec(1) == 1
    assert climb_stairs_rec(2) == 2
    assert climb_stairs_rec(3) == 3
    assert climb_stairs_rec(4) == 5


def test_climb_stairs_iter():
    assert climb_stairs_iter(1) == 1
    assert climb_stairs_iter(2) == 2
    assert climb_stairs_iter(3) == 3
    assert climb_stairs_iter(4) == 5
