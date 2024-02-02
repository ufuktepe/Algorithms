def num_subarray_less_than_k(nums, k):
    i, j = 0, 0
    cur_product = 1
    count = 0

    while j < len(nums):
        cur_product *= nums[j]

        while cur_product >= k:
            cur_product = cur_product / nums[i]
            i += 1

        if cur_product < k:
            count += j - i + 1

        j += 1
    return count


def test():
    nums = [10, 5, 2, 6]
    k = 100
    assert num_subarray_less_than_k(nums, k) == 8
