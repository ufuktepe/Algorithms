# Time: O(n^2)  Space: O(n) due to sorting
def three_sum_closest(nums, target):
    closest = float('inf')

    # O(n*log(n))
    nums.sort()

    def get_closest(target, i, j):
        cur_sum, best_sum = None, float('inf')

        while i < j:
            cur_sum = nums[i] + nums[j]
            if abs(target - cur_sum) < abs(target - best_sum):
                best_sum = cur_sum

            if cur_sum == target:
                return target
            elif target < cur_sum:
                j -= 1
            else:
                i += 1

        return best_sum

    # O(n^2)
    for i in range(len(nums) - 2):
        num = nums[i]
        cur_target = target - num
        cur_closest = get_closest(cur_target, i + 1, len(nums) - 1)

        if abs(target - closest) > abs(target - cur_closest - num):
            closest = cur_closest + num

    return closest


def test():
    assert three_sum_closest([1, 2, 5, 7], 10) == 10
    assert three_sum_closest([5, 3, 1, -1, 10], 7) == 7
    assert three_sum_closest([5, 3, 1, -1, 8], 7) == 7