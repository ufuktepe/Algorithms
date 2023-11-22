def find_median_sorted_arrays(nums1, nums2):
    def solve(k, a_start, a_end, b_start, b_end):
        if a_start > a_end:
            return nums2[k - a_start]     # So far we have eliminated a_start items from nums1
        if b_start > b_end:
            return nums1[k - b_start]  # So far we have eliminated ba_start items from nums2

        a_mid_idx = (a_start + a_end) // 2
        b_mid_idx = (b_start + b_end) // 2

        a_mid_val = nums1[a_mid_idx]
        b_mid_val = nums2[b_mid_idx]

        if k > (a_mid_idx + b_mid_idx):
            # Discard the smaller left half
            if a_mid_val < b_mid_val:
                return solve(k, a_mid_idx + 1, a_end, b_start, b_end)
            else:
                return solve(k, a_start, a_end, b_mid_idx + 1, b_end)
        else:  # k <= (a_mid_idx + b_mid_idx)
            # Discard the bigger right half
            if a_mid_val < b_mid_val:
                return solve(k, a_start, a_end, b_start, b_mid_idx - 1)
            else:
                return solve(k, a_start, a_mid_idx - 1, b_start, b_end)

    n = len(nums1) + len(nums2)

    if n % 2 == 0:
        first_num = solve(n // 2 - 1, 0, len(nums1) - 1, 0, len(nums2) - 1)
        second_num = solve(n // 2, 0, len(nums1) - 1, 0, len(nums2) - 1)
        return (first_num + second_num) / 2
    else:
        return solve(n // 2, 0, len(nums1) - 1, 0, len(nums2) - 1)


def find_median_sorted_arrays_v2(nums1, nums2):

    def solve(k):
        left_a = left_b = 0
        right_a = len(nums1) - 1
        right_b = len(nums2) - 1

        while left_a <= right_a and left_b <= right_b:
            mid_a = (left_a + right_a) // 2
            mid_b = (left_b + right_b) // 2

            mid_a_val = nums1[mid_a]
            mid_b_val = nums2[mid_b]

            num_of_left_items = mid_a + mid_b

            if k <= num_of_left_items:
                # Discard the right half that starts with the larger number
                if mid_a_val > mid_b_val:
                    right_a = mid_a - 1
                else:
                    right_b = mid_b - 1
            elif k > num_of_left_items:
                # Discard the left half that starts with the smaller number
                if mid_a_val < mid_b_val:
                    left_a = mid_a + 1
                else:
                    left_b = mid_b + 1

        if left_a > right_a:
            # We have eliminated left_a items from nums1
            return nums2[k - left_a]
        else:
            return nums1[k - left_b]

    n1 = len(nums1)
    n2 = len(nums2)
    n = n1 + n2

    if n % 2 == 0:
        first_num = solve(n // 2 - 1)
        second_num = solve(n // 2)
        return (first_num + second_num) / 2
    else:
        return solve(n // 2)

def test_1():
    nums1 = [4, 8, 10]
    nums2 = [2, 7, 9]
    assert find_median_sorted_arrays_v2(nums1, nums2) == 7.5