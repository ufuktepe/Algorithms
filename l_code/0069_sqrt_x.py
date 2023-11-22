def my_sqrt(x):
    left = 0
    right = x

    while left <= right:
        mid = (left + right) // 2

        if x == mid ** 2:
            return mid
        elif x < mid ** 2:
            right = mid - 1
        else:
            left = mid + 1

    return right


def test_1():
    assert my_sqrt(3) == 1
    assert my_sqrt(2) == 1
    assert my_sqrt(1) == 1