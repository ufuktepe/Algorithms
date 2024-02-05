# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
# class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

def get_peak_index(arr):
    left, right = 0, arr.length() - 1

    while left < right:
        mid = (left + right) // 2

        if arr.get(mid + 1) > arr.get(mid):
            left = mid + 1
        else:
            right = mid

    return left


def find_left(arr, left, right, target):
    while left <= right:
        mid = (left + right) // 2

        if arr.get(mid) == target:
            return mid
        elif arr.get(mid) < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def find_right(arr, left, right, target):
    while left <= right:
        mid = (left + right) // 2

        if arr.get(mid) == target:
            return mid
        elif arr.get(mid) > target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        p_index = get_peak_index(mountain_arr)

        left_idx = find_left(mountain_arr, 0, p_index, target)
        if left_idx != -1:
            return left_idx

        return find_right(mountain_arr, p_index, mountain_arr.length() - 1, target)