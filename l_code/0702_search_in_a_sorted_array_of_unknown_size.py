class ArrayReader:
    def __init__(self, items):
        self.items = items

    def get(self, index: int) -> int:
        if index > len(self.items):
            return 2 ** 31 - 1
        return self.items[index]


# Time: O(log(10000))
def search(reader, target):
    left = 0
    right = 10 ** 4
    out_of_bounds = 2 ** 31 - 1

    while left <= right:
        mid = (left + right) // 2
        cur = reader.get(mid)

        if cur == target:
            return mid
        elif cur == out_of_bounds or cur > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1


def test_1():
    reader = ArrayReader([-1, 0, 3, 5, 9, 12])
    assert search(reader, 9) == 4
