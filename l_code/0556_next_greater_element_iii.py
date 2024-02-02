# Time: O(n)  Space: O(n)
def nge(n):
    nums = [int(digit) for digit in str(n)]
    stack = []
    j = k = None

    # O(n)
    for i in range(len(nums) - 1, -1, -1):
        while stack and nums[i] < nums[stack[-1]]:
            j = stack.pop()

        if j is not None:
            # swap
            k = i
            nums[k], nums[j] = nums[j], nums[k]
            break

        stack.append(i)

    # O(n)
    if j is None:
        return -1
    else:
        left, right = k + 1, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

    # O(n)
    next_n = int(''.join([str(digit) for digit in nums]))

    MAX = 2 ** 31
    MIN = -2 ** 31 - 1

    next_n = max(MIN, min(next_n, MAX))

    return next_n if MIN < next_n < MAX else -1


def test():
    assert nge(21) == -1
    assert nge(12) == 21
    assert nge(15432) == 21345