def move_zeroes(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """

    j = 0

    for i in range(len(nums) - 1):
        if nums[i] == 0:
            if j < i:
                j = i + 1

            while nums[j] == 0:
                j += 1
                if j == len(nums):
                    return

            nums[i], nums[j] = nums[j], nums[i]

    return nums


def moveZeroes(nums):
    anchor = 0
    for explorer in range(len(nums)):
        if nums[explorer] != 0:
            nums[anchor], nums[explorer] = nums[explorer], nums[anchor]
            anchor += 1


# def test_1_item():
#     nums = [0]
#     move_zeroes(nums)
#     assert nums == [0]
#
#
# def test_2_items():
#     nums = [1, 0]
#     move_zeroes(nums)
#     assert nums == [1, 0]
#
#
# def test_5_items():
#     nums = [0, 1, 0, 3, 12]
#     move_zeroes(nums)
#     assert nums == [1, 3, 12, 0, 0]

moveZeroes([1, 2, 0, 0, 5, 6, 0])