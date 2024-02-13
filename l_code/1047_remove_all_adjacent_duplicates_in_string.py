# Time: O(n)  Space: O(n)
def remove_dups(s):
    stack = []

    for ch in s:
        if stack and stack[-1] == ch:
            stack.pop()
        else:
            stack.append(ch)

    return ''.join(stack)


def test():
    assert remove_dups('abc') == 'abc'
    assert remove_dups('a') == 'a'
    assert remove_dups('xyyc') == 'xc'
    assert remove_dups('abcddcbaxy') == 'xy'
    assert remove_dups('abcddcba') == ''