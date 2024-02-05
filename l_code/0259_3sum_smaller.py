def threeSumSmaller(nums, target):
    def get_num_of_smaller_triplets(i):
        count = 0
        j = i + 1
        k = len(nums) - 1

        while j < k:
            if nums[i] + nums[j] + nums[k] < target:
                count += k - j
                j += 1
            else:
                k -= 1

        return count

    count = 0
    nums.sort()
    for i in range(len(nums) - 2):
        count += get_num_of_smaller_triplets(i)

    return count


def test():
    nums = [1,-1,2,0,3,-2]
    target = 2
    assert threeSumSmaller(nums, target) == 10