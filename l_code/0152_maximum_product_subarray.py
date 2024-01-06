# Time: O(n)  Space: O(n) where n is the length of nums array
def max_product_subarray(nums):
    n = len(nums)

    # dp_max[i] is the largest product of a subarray that ends at index i
    dp_max = [0] * n

    # dp_max[i] is the smallest product of a subarray that ends at index i
    dp_min = [0] * n

    # Base cases
    dp_max[0] = nums[0]
    dp_min[0] = nums[0]

    max_product = nums[0]

    for i in range(1, n):
        dp_max[i] = max(nums[i], dp_max[i - 1] * nums[i], dp_min[i - 1] * nums[i])
        dp_min[i] = min(nums[i], dp_max[i - 1] * nums[i], dp_min[i - 1] * nums[i])
        max_product = max(max_product, dp_max[i])

    return max_product


def test():
    nums = [9, -1, -1, 9]
    assert max_product_subarray(nums) == 81


def test_2():
    nums = [9, 0, -1, 9]
    assert max_product_subarray(nums) == 9