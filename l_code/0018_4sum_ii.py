from collections import defaultdict


# Time: O(n^2)  Space: O(n^2)
def four_count(nums1, nums2, nums3, nums4):
    freq = defaultdict(int)
    for num3 in nums3:
        for num4 in nums4:
            freq[(num3 + num4)] += 1

    res = 0
    for num1 in nums1:
        for num2 in nums2:
            res += freq[-(num1 + num2)]

    return res


def k_count(num_lsts):
    def sum_count(lsts):
        freq = {0: 1}
        for lst in lsts:
            temp_freq = defaultdict(int)
            for num in lst:
                for total in freq:
                    temp_freq[total+num] += freq[total]
            freq = temp_freq

        return freq

    n = len(num_lsts)
    left_lists = num_lsts[:n // 2]
    right_lists = num_lsts[n // 2:]

    left_freq = sum_count(left_lists)
    right_freq = sum_count(right_lists)

    res = 0

    for total, freq1 in left_freq.items():
        if -total in right_freq:
            res += freq1 * right_freq[-total]

    return res


def test():
    nums1 = [1, 2]
    nums2 = [-2, -1]
    nums3 = [-1, 2]
    nums4 = [0, 2]
    assert four_count(nums1, nums2, nums3, nums4) == 2
    assert k_count([nums1, nums2, nums3, nums4]) == 2