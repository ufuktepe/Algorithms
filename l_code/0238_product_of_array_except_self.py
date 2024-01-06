# Time: O(n)  Space: O(1)
def product_except_self(nums):
    n = len(nums)
    res = [1] * n

    for i in range(1, n):
        res[i] = res[i - 1] * nums[i - 1]

    prev = 1
    for i in range(n - 1, -1, -1):
        res[i] *= prev
        prev *= nums[i]

    return res


def test():
    nums = [1, 2, 3, 4]
    assert product_except_self(nums) == [24, 12, 8, 6]


def test_2():
    nums = [1, 0, 3, 4]
    assert product_except_self(nums) == [0, 12, 0, 0]