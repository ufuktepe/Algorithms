from collections import deque
import heapq


# Time: O(n*log(n))  Space: O(n)
def smallest_range(nums):
    k = len(nums)
    points = []

    for i, nums_lst in enumerate(nums):
        for num in nums_lst:
            points.append((num, i))

    # O(n*log(n))
    points.sort()
    q = deque()
    last_vals = {i: None for i in range(k)}
    min_delta = float('inf')
    ans = None

    seen = set()

    for num, i in points:
        q.append((num, i))
        last_vals[i] = num
        seen.add(i)

        while q[0][0] != last_vals[q[0][1]]:
            q.popleft()

        if len(seen) == k:
            delta = q[-1][0] - q[0][0]
            if min_delta > delta:
                min_delta = delta
                ans = [q[0][0], q[-1][0]]

    return ans


class Solution:
    def smallestRange(self, nums):
        heap=[]
        maxvalue=0
        for i in range(len(nums)):
            heapq.heappush(heap,[nums[i][0],i,0])
            maxvalue=max(maxvalue,nums[i][0])
        answer=[heap[0][0],maxvalue]
        while True:
            _,row,col=heapq.heappop(heap)
            if col==len(nums[row])-1:
                break
            next_num=nums[row][col+1]
            heapq.heappush(heap,[next_num,row,col+1])
            maxvalue=max(maxvalue,next_num)
            if maxvalue-heap[0][0]<answer[1]-answer[0]:
                answer=[heap[0][0],maxvalue]
        return answer

def test():
    nums = [[2, 10, 19],[4, 14, 15, 16],[8, 12, 17]]
    assert smallest_range(nums) == [16, 19]