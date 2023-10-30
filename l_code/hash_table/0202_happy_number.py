def is_happy(n):
    """
    :type n: int
    :rtype: bool
    """
    seen = set()
    while n != 1:
        s = 0
        for digit in str(n):
            s += int(digit) ** 2
        if s in seen:
            return False
        seen.add(s)
        n = s

    return True


def test_happy():
    assert is_happy(7) == True


def test_unhappy():
    assert is_happy(2) == False
