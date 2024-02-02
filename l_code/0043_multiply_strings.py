def get_str_from_num_value(num_val):
    int_to_str = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    res = []

    while num_val > 0:
        digit = num_val % 10
        res.append(int_to_str[digit])
        num_val //= 10

    return ''.join(res[::-1]) if res else '0'


def get_num_value_from_str(num):
    ints = {'0': 0,
            '1': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9}
    val = 0

    for i, digit in enumerate(num[::-1]):
        digit_val = ints[digit]
        val += digit_val * 10 ** i
    return val


# Time: O(n) where n is the max num of digits among num1 and num2. Or O(log(max(num1, num2)))
# Space: O(1)
def multiply(num1, num2):
    num1_val = get_num_value_from_str(num1)
    num2_val = get_num_value_from_str(num2)
    res_val = num1_val * num2_val

    return get_str_from_num_value(res_val)


def test():
    assert multiply('2', '3') == '6'
    assert multiply('20', '15') == '300'
    assert multiply('7', '80') == '560'
    assert multiply('11', '11') == '121'
    assert multiply('0', '11') == '0'