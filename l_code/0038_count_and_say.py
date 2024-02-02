def count_and_say(n):
    if n == 1:
        return '1'

    digit = '1'
    for _ in range(1, n):
        cur_digit = None
        count = 0
        temp = []
        for i in range(len(digit)):
            if not cur_digit or cur_digit == digit[i]:
                cur_digit = digit[i]
                count += 1
            else:
                temp.append(str(count))
                temp.append(cur_digit)
                cur_digit = digit[i]
                count = 1

        temp.append(str(count))
        temp.append(cur_digit)

        digit = ''.join(temp)

    return digit


def test():
    assert count_and_say(1) == '1'
    assert count_and_say(2) == '11'
    assert count_and_say(3) == '21'
    assert count_and_say(4) == '1211'
