# O(n) solution
def twoSumV2(numbers, target):
    """
    :type numbers: List[int]
    :type target: int
    :rtype: List[int]
    """
    l = 0
    r = len(numbers) - 1

    while l < r:
        temp_sum = numbers[l] + numbers[r]
        if temp_sum == target:
            return [l + 1, r + 1]
        elif temp_sum < target:
            l += 1
        else:
            r -= 1


# O(n^2) solution
def twoSum(numbers, target):
    """
    :type numbers: List[int]
    :type target: int
    :rtype: List[int]
    """
    for i in range(len(numbers) - 1):
        if i != 0 and numbers[i] == numbers[i - 1]:
            continue
        for j in range(i+1, len(numbers)):
            if (numbers[i] + numbers[j]) == target:
                return [i+1, j+1]
            if (numbers[i] + numbers[j]) > target:
                break


def test_array_with_2_numbers():
    numbers = [-1, 0]
    target = -1
    assert twoSumV2(numbers, target) == [1, 2]


def test_array_with_3_numbers():
    numbers = [2, 5, 6]
    target = 8
    assert twoSumV2(numbers, target) == [1, 3]


def test_array_with_4_numbers():
    numbers = [2, 7, 11, 15]
    target = 26
    assert twoSumV2(numbers, target) == [3, 4]


def test_array_with_5_numbers():
    numbers = [10, 13, 21, 44, 100]
    target = 113
    assert twoSumV2(numbers, target) == [2, 5]