# Time: O(N)  Space: O(N)
def get_num_of_ways(n, k):
    # dp_1[i] is the num of ways we can paint i fence posts with k colors where the last 2 colors are different
    dp_1 = [0] * max((n + 1), 4)
    # dp_2[i] is the num of ways we can paint i fence posts with k colors where the last 2 colors are the same
    dp_2 = [0] * max((n + 1), 4)

    # Base cases
    dp_1[1] = k
    dp_1[2] = k ** 2 - k
    dp_2[2] = k

    for i in range(3, n + 1):
        dp_1[i] = (dp_2[i - 1] + dp_1[i - 1]) * (k - 1)
        dp_2[i] = dp_1[i - 1]

    return dp_1[n] + dp_2[n]


def test():
    n = 3
    k = 2
    assert get_num_of_ways(n, k) == 6


def test_2():
    n = 7
    k = 2
    assert get_num_of_ways(n, k) == 42