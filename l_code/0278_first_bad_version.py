def isBadVersion(x):
    n = 2
    return x >= n


def first_bad_version(n):
    left = 1
    right = n

    while left <= right:
        mid = (left + right) // 2
        is_bad = isBadVersion(mid)
        if not is_bad:
            left = mid + 1
        else:
            right = mid - 1

    if left <= n:
        return left
    return -1


def test_1():
    assert first_bad_version(2) == 2