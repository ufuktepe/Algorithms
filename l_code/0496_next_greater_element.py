# Let len(nums2) be n and len(nums1) be m, so n > m
# Time: O(n)  Space: O(n)
def nge(nums1, nums2):
    def get_nge(nums):
        n = len(nums)
        res = [-1] * n
        stack = []  # invariant: the values corresponding to indexes are always in decreasing order

        for i, num in enumerate(nums):
            while stack and nums[stack[-1]] < num:
                idx = stack.pop()
                res[idx] = num

            stack.append(i)

        return res

    nge = get_nge(nums2)

    nums2_map = {}
    for i, num in enumerate(nums2):
        nums2_map[num] = i

    res = []
    for num in nums1:
        idx = nums2_map[num]
        res.append(nge[idx])

    return res


def test():
    nums1 = [4, 1, 2]
    nums2 = [1, 3, 4, 2]
    assert nge(nums1, nums2) == [-1, 3, -1]