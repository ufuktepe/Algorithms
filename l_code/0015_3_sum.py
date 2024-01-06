from collections import defaultdict


def three_sum(nums):
    counter = defaultdict(int)

    # O(n)
    for i, num in enumerate(nums):
        counter[num] += 1

    n = len(nums)
    triplets = set()

    for i in range(n - 1):
        for j in range(i + 1, n):
            val = (nums[i] + nums[j]) * -1

            triplet = [nums[i], nums[j], val]
            triplet.sort()
            triplet = tuple(triplet)

            if triplet in triplets:
                continue

            counter[nums[i]] -= 1
            counter[nums[j]] -= 1

            if counter[val] > 0:
                triplets.add(triplet)

            counter[nums[i]] += 1
            counter[nums[j]] += 1

    return [list(triplet) for triplet in triplets]


def three_sum_two_pointers(nums):
    nums.sort()
    res = []

    def two_sum(j, num1):
        lo = j
        hi = len(nums) - 1

        while lo < hi:
            if num1 + nums[lo] + nums[hi] == 0:
                res.append([num1, nums[lo], nums[hi]])
                return
            if num1 + nums[lo] + nums[hi] < 0:
                lo += 1
            elif num1 + nums[lo] + nums[hi] > 0:
                hi -= 1

    for i, num1 in enumerate(nums):
        if i == 0 or nums[i - 1] != nums[i]:
            two_sum(i + 1, num1)

    return res


def test():
    nums = [-1, 0, 1, 2, -1, -4]
    assert three_sum(nums) == [[-1, 0, 1], [-1, -1, 2]]
