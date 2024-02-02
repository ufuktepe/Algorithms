# Time: O(n^2)  Space: O(1)
def next_permutation(nums):
    n = len(nums)

    if n < 2:
        return nums

    def increase():
        i = len(nums) - 2
        min_largest_index = None

        while i >= 0:
            cur = nums[i]
            for j in range(i + 1, len(nums)):
                if nums[j] > cur and (min_largest_index is None or nums[min_largest_index] > nums[j]):
                    min_largest_index = j

            if min_largest_index:
                nums[i], nums[min_largest_index] = nums[min_largest_index], nums[i]
                return i

            i -= 1

        return None

    def partition(left, right):
        pivot = nums[right]
        i = left - 1

        for j in range(left, right):
            if nums[j] < pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]

        nums[right], nums[i + 1] = nums[i + 1], nums[right]

        return i + 1

    def quick_sort(left, right):
        if left < right:
            idx = partition(left, right)
            quick_sort(left, idx - 1)
            quick_sort(idx + 1, right)

    i = increase()

    if i is None:
        quick_sort(0, n - 1)
    else:
        quick_sort(i + 1, n - 1)


# Time: O(n)  Space: O(1)
def next_permutation_v2(nums):
    def reverse(i):
        left = i
        right = len(nums) - 1

        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

    n = len(nums)
    p = None
    q = None
    for i in range(n - 1, 0, -1):
        if nums[i - 1] < nums[i]:
            p = i - 1
            # Find the smallest number that is larger than nums[i - 1] in nums[i:]
            for j in range(i, n):
                if nums[p] < nums[j]:
                    q = j
                else:
                    break
            nums[p], nums[q] = nums[q], nums[p]
            break

    if p is None:
        reverse(0)
    else:
        reverse(p + 1)



def test():
    nums = [3, 1, 2]
    next_permutation_v2(nums)
    assert nums == [3, 2, 1]


def test_2():
    nums = [3, 2, 1]
    next_permutation_v2(nums)
    assert nums == [1, 2, 3]


def test_3():
    nums = [1, 3, 4, 2]
    next_permutation_v2(nums)
    assert nums == [1, 4, 2, 3]