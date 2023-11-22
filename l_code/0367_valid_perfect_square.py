# Time: O(log(num))  Space: O(1)
def is_perfect_square(num):
    if num == 1:
        return True
    left = 1
    right = num // 2

    # O(log(num))
    while left <= right:
        mid = (left + right) // 2
        mid_squared = mid ** 2

        if num == mid_squared:
            return True
        elif num > mid_squared:
            left = mid + 1
        else:
            right = mid - 1
    return False


def test_1():
    assert is_perfect_square(1) == True
    assert is_perfect_square(2) == False
    assert is_perfect_square(3) == False
    assert is_perfect_square(4) == True
    assert is_perfect_square(80) == False
    assert is_perfect_square(81) == True
