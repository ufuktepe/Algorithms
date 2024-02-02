# Time: O(n)  Space: O(1)
def find_missing_ranges(nums, lower, upper):
    def get_range(left, right):
        if left > right:
            return []
        return [left, right]

    if len(nums) == 0:
        return [get_range(lower, upper)]

    res = []

    missing_left = get_range(lower, nums[0] - 1)
    if missing_left:
        res.append(missing_left)

    for i in range(len(nums) - 1):
        missing = get_range(nums[i] + 1, nums[i + 1] - 1)
        if missing:
            res.append(missing)

    missing_right = get_range(nums[-1] + 1, upper)
    if missing_right:
        res.append(missing_right)

    return res


def test():
    nums = [2, 4, 9]
    lower = 1
    upper = 9

    assert find_missing_ranges(nums, lower, upper) == [[1, 1], [3, 3], [5, 9]]