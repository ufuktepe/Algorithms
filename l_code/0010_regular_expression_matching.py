def is_match(s, p):


    def get_chars(i):
        if i == len(p):
            return None, None

        if p[i] == '*':
            next = p[i + 1] if i + 1 < len(p) else None
            prev = p[i - 1] if i - 1 >= 0 else None

            return prev, next

        return None, None

    def _is_match(s, p, i):
        prev, next = get_chars(i)
        j = 0

        while i < len(p) and j < len(s):
            ch = s[j]
            if p[i] == '.':
                prev, next = get_chars(i)
                i += 1
                j += 1
    
            elif p[i] == '*':
                if ch == prev:
                    j += 1
                elif ch == next or next == '.':
                    prev, next = get_chars(i + 1)
                    i += 2
                    j += 1
                elif prev == '.':
                    j += 1
                else:
                    j = 0

            elif p[i] == ch:
                prev, next = get_chars(i)
                i += 1
            else:
                return False

            j += 1

    for i in range(p):
        if _is_match(s, p, i):
            return True

    return False


def test():
    s = 'ab'
    p = '.*'
    assert is_match(s, p)


def test_2():
    s = 'aa'
    p = 'a'
    assert is_match(s, p) is False


def test_3():
    s = 'abcde'
    p = 'a.*de'
    assert is_match(s, p)