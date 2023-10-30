def addBinary(a, b):
    """
    :type a: str
    :type b: str
    :rtype: str
    """
    if b == '':
        return a

    i = len(a) - 1
    j = len(b) - 1
    carry = 0
    output = []

    while True:
        val_a = 0 if i < 0 else int(a[i])
        val_b = 0 if j < 0 else int(b[j])
        sum_val = val_a + val_b + carry
        output.append(sum_val % 2)
        carry = 1 if sum_val > 1 else 0

        if carry == 0 and i <= 0 and j <= 0:
            break

        i -= 1
        j -= 1

    output.reverse()
    return ''.join(str(c) for c in output)


def test_1_and_1():
    a = '1'
    b = '1'
    assert addBinary(a, b) == '10'


def test_10_and_1():
    a = '10'
    b = '1'
    assert addBinary(a, b) == '11'


def test_11_and_1():
    a = '11'
    b = '1'
    assert addBinary(a, b) == '100'


def test_111_and_10():
    a = '111'
    b = '10'
    assert addBinary(a, b) == '1001'