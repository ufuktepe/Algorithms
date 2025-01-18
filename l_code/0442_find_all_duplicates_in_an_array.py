# Time: O(n)  Space: O(1)
def duplicates(nums):
    res = []
    for i, num in enumerate(nums):
        if nums[abs(num) - 1] < 0:
            res.append(abs(num))
        else:
            nums[abs(num) - 1] *= -1

    return res



def test():
    nums = [3, 1, 2, 5, 6, 5]
    assert duplicates(nums) == [5]


def test_2():
    nums = [3, 1, 2, 5, 6, 4]
    assert duplicates(nums) == []