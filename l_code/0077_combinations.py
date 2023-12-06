def combine(n, k):
    combinations = []

    def solve(start, k, prefix):
        if k == 0:
            combinations.append(prefix)
            return

        for i in range(start, n + 1):
            new_prefix = prefix + [i]
            solve(i + 1, k - 1, new_prefix)

    solve(1, k, [])
    return combinations


def test():
    assert combine(4, 2) == [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]