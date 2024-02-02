def divide(dividend, divisor):
    MAX = 2 ** 31 - 1
    MIN = -2 ** 31

    mult = 1
    if dividend < 0:
        remaining = -1 * dividend
        mult *= -1
    else:
        remaining = dividend

    if divisor < 0:
        x = -1 * divisor
        mult *= -1
    else:
        x = divisor

    def get_rem_and_q(total, x):
        if total < x:
            return total, 0

        cur_q = 1
        q = 0
        while total >= x:
            total -= x
            x += x
            q += cur_q
            cur_q += cur_q

        return total, q

    total_q = 0
    while remaining >= x:
        remaining, quotient = get_rem_and_q(remaining, x)
        total_q += quotient

    res = total_q * mult

    if res < MIN:
        return MIN

    if res > MAX:
        return MAX

    return res


def test():
    assert divide(1, 2) == 0
    assert divide(2, 2) == 1
    assert divide(2, -2) == -1
    assert divide(-2, 2) == -1
    assert divide(-2, -2) == 1
    assert divide(-10, 3) == -3