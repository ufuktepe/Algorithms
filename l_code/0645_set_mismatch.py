# Time: O(n)  Space: O(n)
def find_error(nums):
    seen = set()
    all_nums = {i + 1 for i in range(len(nums))}
    res = []

    for num in nums:
        if num in seen:
            res.append(num)
        else:
            all_nums.remove(num)

        seen.add(num)

    res.append(list(all_nums)[0])

    return res


def find_error_const_space(nums):
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    dup = None
    actual_sum = 0
    for num in nums:
        pos_num = abs(num)
        actual_sum += pos_num
        if nums[pos_num - 1] < 0:
            dup = pos_num
        else:
            nums[pos_num - 1] *= -1

    missing = expected_sum - actual_sum + dup

    return [dup, missing]


def test():
    nums = [1, 2, 3, 3, 5, 6, 7]
    assert find_error_const_space(nums) == [3, 4]

