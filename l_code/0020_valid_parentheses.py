def is_valid(s):
    stack = []

    open_chars = '[({'
    char_map = {']': '[', ')': '(', '}': '{'}

    for ch in s:
        if ch in open_chars:
            stack.append(ch)
        else:
            if len(stack) == 0 or stack[-1] != char_map[ch]:
                return False
            stack.pop()

    return len(stack) == 0


def test_valid():
    s = '([[{()}]])'
    assert is_valid(s)


def test_invalid():
    s = '([[{()}])'
    assert is_valid(s) == False