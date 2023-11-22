def pow(x, n):

    def binary_exp(x, n):
        if n == 0:
            return 1
        elif n % 2 == 0:
            return binary_exp(x * x, n // 2)
        else:
            return x * binary_exp(x * x, (n - 1) // 2)

    res = binary_exp(x, abs(n))
    return res if n >= 0 else 1/res


def test_1():
    assert pow(3, 4) == 81
    assert pow(1, 3) == 1
    assert pow(0, 3) == 0
    assert pow(-2, 5) == -32
    assert pow(2, -4) == 1/16