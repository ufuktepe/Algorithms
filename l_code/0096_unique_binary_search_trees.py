from functools import lru_cache


# Time: O(n^3)  Space: O(n^2)
def num_trees(n):
    @lru_cache(maxsize=None)
    def traverse(i):
        if i == 0:
            return 1

        total = 0
        for k in range(1, i + 1):
            n_left_trees = traverse(k - 1)
            n_right_trees = traverse(i - k)

            total += (n_left_trees * n_right_trees)

        return total

    return traverse(n)


def test():
    assert num_trees(1) == 1