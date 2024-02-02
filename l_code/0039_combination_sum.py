def combination_sum(candidates, target):
    candidates.sort()  # <-- This can be removed. Added to simplify the testing.
    res = []
    cur = []

    def visit(i, total):
        cur.append(candidates[i])
        total += candidates[i]

        if total == target:
            res.append([val for val in cur])
        else:
            for j in range(i, len(candidates)):
                if total + candidates[j] <= target:
                    total = visit(j, total)

        cur.remove(candidates[i])
        total -= candidates[i]
        return total

    for i, candidate in enumerate(candidates):
        if candidate <= target:
            visit(i, 0)

    return res


def test():
    candidates = [1, 2, 3]
    target = 4
    assert combination_sum(candidates, target) == [[1, 1, 1, 1], [1, 1, 2], [1, 3], [2, 2]]


def test_2():
    candidates = [6, 8, 10, 4]
    target = 12
    assert combination_sum(candidates, target) == [[4, 4, 4], [4, 8], [6, 6]]