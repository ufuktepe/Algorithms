# Time O(n)  Space: O(n)
def nge(nums):
    n = len(nums)
    res = [-1] * n
    stack = []  # values of the indices are always in non-increasing order

    for i, num in enumerate(nums):
        while stack and nums[stack[-1]] < num:
            idx = stack.pop()
            res[idx] = num
        stack.append(i)

    if stack:
        for i in range(stack[0] + 1):
            while stack and nums[stack[-1]] < nums[i]:
                idx = stack.pop()
                res[idx] = nums[i]

    return res


def test():
    assert nge([13, 10, 8, 9, 12]) == [-1, 12, 9, 12, 13]