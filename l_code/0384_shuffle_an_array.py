import random


class Solution:
    # Initializes the object with the integer array nums.
    # O(n)
    def __init__(self, nums):
        self.orig_nums = nums[:]
        self.nums = nums
        self.n = len(nums)

    # Resets the array to its original configuration and returns it.
    # O(n)
    def reset(self):
        self.nums = self.orig_nums[:]
        return self.nums

    # Returns a random shuffling of the array.
    # O(n)
    def shuffle(self):
        j = self.n - 1
        for _ in range(self.n - 1):
            i = random.randint(0, j)
            self.nums[i], self.nums[j] = self.nums[j], self.nums[i]
            j -= 1

        return self.nums


sltn = Solution([1, 2, 3, 4, 5, 6, 7])
print(sltn.shuffle())
print(sltn.reset())
