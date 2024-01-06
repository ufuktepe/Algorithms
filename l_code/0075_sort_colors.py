# Time: O(n)  Space: O(1)
def sort_colors(nums):
    colors = [0, 0, 0]

    for num in nums:
        colors[num] += 1

    counter = 0
    for color, count in enumerate(colors):
        for i in range(count):
            nums[counter] = color
            counter += 1


def sort_colors_2(nums):
    p0 = cur = 0
    p2 = len(nums) - 1

    while cur <= p2:
        if nums[cur] == 0:
            nums[p0], nums[cur] = nums[cur], nums[p0]
            p0 += 1
            cur += 1
        elif nums[cur] == 1:
            cur += 1
        else:
            nums[cur], nums[p2] = nums[p2], nums[cur]
            p2 -= 1


def test():
    nums = [0, 1, 2, 0, 1]
    sort_colors_2(nums)
    assert nums == [0, 0, 1, 1, 2]


def test_2():
    nums = [0, 2, 2, 0, 2, 1, 1, 0]
    sort_colors_2(nums)
    assert nums == [0, 0, 0, 1, 1, 2, 2, 2]