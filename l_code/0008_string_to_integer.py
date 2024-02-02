# Time and Space: O(n)
def my_atoi(s):
    def sanitize(input_s):
        DIGITS = '0123456789'
        SIGNS = '+-'
        n = len(input_s)
        i = 0
        found_digit = False
        res = []

        while i < n:
            if not found_digit:
                if input_s[i] in DIGITS or input_s[i] in SIGNS:
                    res.append(input_s[i])
                    found_digit = True
                elif input_s[i] != ' ':
                    break
            elif input_s[i] in DIGITS:
                res.append(input_s[i])
            else:
                break
            i += 1

        return res if found_digit else ['0']

    sanitized = sanitize(s)
    n = len(sanitized)
    i = 0
    sign = 1

    if sanitized[0] == '+':
        i += 1
    elif sanitized[0] == '-':
        sign = -1
        i += 1

    total = 0

    while i < n:
        total *= 10
        total += int(sanitized[i])

        i += 1

    total *= sign

    if total > 2 ** 31 - 1:
        total = 2 ** 31 - 1
    if total < -2 ** 31:
        total = -2 ** 31

    return total


def my_atoi_v2(s):
    found_digit = False
    res = 0
    sign = 1

    for ch in s:
        if not found_digit:
            if ch.isdigit():
                res = res * 10 + int(ch)
                found_digit = True
            elif ch == '+':
                sign = 1
                found_digit = True
            elif ch == '-':
                sign = -1
                found_digit = True
            elif ch != ' ':
                return 0
        elif ch.isdigit():
            res = res * 10 + int(ch)
        else:
            break

    res *= sign
    res = min(res, 2**31 - 1)
    res = max(res, -2 ** 31)

    return res




def test():
    assert my_atoi_v2('   42') == 42
    assert my_atoi_v2('   42  ') == 42
    assert my_atoi_v2('   42asas  ') == 42
    assert my_atoi_v2('   +42  ') == 42
    assert my_atoi_v2('   -42  ') == -42
    assert my_atoi_v2('  asd  ') == 0


def test_2():
    assert my_atoi_v2("+-12") == 0