def permute(nums):
    res = []

    def solve(prefix):
        if len(prefix) == len(nums):
            res.append(prefix[:])
            return

        for num in nums:
            if num in prefix:
                continue
            prefix.append(num)
            solve(prefix)
            prefix.pop()

    solve([])

    return res


def test():
    assert permute([1]) == [[1]]
    assert permute([2, 3]) == [[2, 3], [3, 2]]