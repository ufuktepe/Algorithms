# Let n be the num of digits
# Time: O(n)  Space: O(n)
def reverse(x):
    is_neg = True if x < 0 else False

    # O(n)
    x_str = str(x)

    # O(n)
    x_str_rev = x_str[::-1]

    if is_neg:
        # O(n)
        x_str_rev = x_str_rev[:-1]

    x_rev = int(x_str_rev)

    if not -2 ** 31 <= x_rev < 2 ** 31:
        return 0

    return -x_rev if is_neg else x_rev


# Let n be the num of digits
# Time: O(n)  Space: O(1)
def reverse_v2(x):
    is_neg = x < 0

    x = abs(x)
    res = 0

    bound = 2 ** 31 if is_neg else 2 ** 31 - 1

    # O(n)
    while x > 0:
        digit = x % 10
        res *= 10

        res += digit
        x = x // 10

        if res > bound:
            return 0

    return -res if is_neg else res


def test():
    x = 321
    assert reverse_v2(x) == 123


def test_2():
    x = -321
    assert reverse_v2(x) == -123


def test_3():
    x = 120
    assert reverse_v2(x) == 21


def test_4():
    x = 9999999993
    assert reverse_v2(x) == 0