def min_size_subarray_sum(target, nums):
    i = 0  # i is the index where the min size subarray starts
    j = 0  # j-1 is the index where the min size subarray ends
    cur_sum = 0
    size = float('inf')

    while j < len(nums):
        if cur_sum < target:
            cur_sum += nums[j]
        j += 1

        while cur_sum >= target:
            if size > j - i:
                size = j - i
            cur_sum -= nums[i]
            i += 1

    return 0 if size == float('inf') else size


def test_success_size_is_1():
    nums = [1, 4, 4]
    target = 4
    assert min_size_subarray_sum(target, nums) == 1


def test_success_size_is_2():
    nums = [1, 3, 6, 4]
    target = 10
    assert min_size_subarray_sum(target, nums) == 2


def test_success_size_is_3():
    nums = [1, 1, 2, 2, 6, 4, 4, 1, 7, 3]
    target = 12
    assert min_size_subarray_sum(target, nums) == 3