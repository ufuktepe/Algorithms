# Time: O(m + n)  Space: O(m)
def merge(nums1, nums2, m, n):
    nums_temp = nums1[:m]

    i = j = k = 0

    while i < m and j < n:
        if nums_temp[i] < nums2[j]:
            nums1[k] = nums_temp[i]
            i += 1
        else:
            nums1[k] = nums2[j]
            j += 1
        k += 1

    while i < m:
        nums1[k] = nums_temp[i]
        i += 1
        k += 1

    while j < n:
        nums1[k] = nums2[j]
        j += 1
        k += 1


def merge_constant_space(nums1, nums2, m, n):
    i = m - 1
    j = n - 1
    k = m + n - 1

    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1

    while i >= 0:
        nums1[k] = nums1[i]
        i -= 1
        k -= 1

    while j >= 0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1


def test():
    nums1 = [10, 12, 15, 0, 0]
    nums2 = [1, 21]
    merge_constant_space(nums1, nums2, 3, 2)
    assert nums1 == [1, 10, 12, 15, 21]


def test_2():
    nums1 = [10, 12, 15]
    nums2 = []
    merge_constant_space(nums1, nums2, 3, 0)
    assert nums1 == [10, 12, 15]

