import random

class Solution:
    # Time: O(n)  Space: O(n)
    def __init__(self, w):
        self.indices = [0]
        total = sum(w)
        prev = 0
        for num in w:
            cur = num/total + prev
            self.indices.append(cur)
            prev = cur

    # Time: O(log(n))  Space: O(1)
    def pickIndex(self):
        val = random.random()

        left, right = 0, len(self.indices) - 1
        mid = (left + right) // 2

        while left < right:
            mid = (left + right) // 2
            if self.indices[mid] <= val < self.indices[mid + 1]:
                return mid
            elif self.indices[mid + 1] <= val:
                left = mid + 1
            else:
                right = mid

        return mid


w = [2, 5, 3]
sltn = Solution(w)
for i in range(10):
    print(sltn.pickIndex())