import heapq
from collections import defaultdict


# class FreqStack:
#
#     def __init__(self):
#         """constructs an empty frequency stack."""
#         self.pq = []
#         self.status = {}  # val: time_stamp
#         self.time_stamp = 0
#
#     def push(self, val: int) -> None:
#         """pushes an integer val onto the top of the stack."""
#         self.time_stamp += 1
#         freq = 0
#         if val in self.status:
#             freq, _ = self.status[val]
#         freq += 1
#         heapq.heappush(self.pq, (-freq, -self.time_stamp, val))
#         self.status[val] = (freq, self.time_stamp)
#
#     def pop(self) -> int:
#         """ removes and returns the most frequent element in the stack.
#             If there is a tie for the most frequent element, the element closest to the stack's top is removed and returned."""
#         while True:
#             neg_freq, neg_time_stamp, val = heapq.heappop(self.pq)
#             freq, time_stamp = self.status[val]
#
#             if -neg_time_stamp == time_stamp:
#                 new_freq = freq - 1
#                 if new_freq > 0:
#                     self.status[val] = (new_freq, time_stamp)
#                     heapq.heappush(self.pq, (-freq, -self.time_stamp, val))
#                 return val


class FreqStack:

    def __init__(self):
        """constructs an empty frequency stack."""
        self.pq = []
        self.history = defaultdict(list)  # val: [(freq1, time_stamp1), (freq2, time_stamp2), ...]
        self.time_stamp = 0

    # O(log(n))
    def push(self, val: int) -> None:
        """pushes an integer val onto the top of the stack."""
        self.time_stamp += 1
        cur_freq = 0
        if self.history[val]:
            cur_freq, _ = self.history[val][-1]

        new_freq = cur_freq + 1
        heapq.heappush(self.pq, (-new_freq, -self.time_stamp, val))
        self.history[val].append((new_freq, self.time_stamp))

    # O(log(n))
    def pop(self) -> int:
        """ removes and returns the most frequent element in the stack.
            If there is a tie for the most frequent element, the element closest to the stack's top is removed and returned."""

        neg_freq, neg_time_stamp, val = heapq.heappop(self.pq)
        self.history[val].pop()
        return val


def test():
    freq_stack = FreqStack()
    nums = [5, 7, 5, 7, 4, 5]
    for num in nums:
        freq_stack.push(num)
    assert freq_stack.pop() == 5
    assert freq_stack.pop() == 7