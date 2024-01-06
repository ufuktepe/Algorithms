# Time O(log(x)) Space: O(1)
def is_palindrome(x: int):
    if x < 0:
        return False
    res = 0
    y = x
    while y > 0:
        digit = y % 10

        res *= 10
        res += digit

        y = y // 10

    return x == res


def test():
    assert is_palindrome(1)
    assert is_palindrome(-1) is False
    assert is_palindrome(12) is False
    assert is_palindrome(525)
    assert is_palindrome(6226)
    assert is_palindrome(123421) is False