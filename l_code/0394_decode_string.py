def decodeString(s):
    """
    :type s: str
    :rtype: str
    """
    chars = []
    nums = []
    cur_num = []

    for ch in s:
        if ch.isdigit():
            cur_num.append(ch)

        elif ch == '[':
            num = int(''.join(cur_num))
            nums.append(num)
            chars.append([])
            cur_num = []

        elif ch == ']':
            num = nums.pop()
            local_chars = chars.pop()
            extended_local_chars = []
            for i in range(num):
                extended_local_chars.extend(local_chars)

            if chars:
                chars[-1].extend(extended_local_chars)
            else:
                chars.append(extended_local_chars)

        else:
            if len(chars) == 0:
                chars.append([])
            chars[-1].append(ch)

    return ''.join(chars[0])


def test_1():
    s = '3[a]'
    assert decodeString(s) == 'aaa'


def test_2():
    s = '2[b]2[a]'
    assert decodeString(s) == 'bbaa'


def test_3():
    s = '1[a2[b]3[a]]'
    assert decodeString(s) == 'abbaaa'


def test_4():
    s = '2[a2[b3[a]]]'
    assert decodeString(s) == 'abaaabaaaabaaabaaa'