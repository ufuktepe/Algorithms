# Time O(n)  Space: O(n)
def get_string(s):
    stack = []

    for ch in s:
        if ch == '#':
            if stack:
                stack.pop()
        else:
            stack.append(ch)

    return ''.join(stack)


def get_next_char(inp, i):
    if i == -1:
        return -1
    count = 0
    while i >= 0:
        if inp[i] == '#':
            count += 1
        elif count > 0:
            count -= 1
        else:
            break
        i -= 1

    return i

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        return get_string(s) == get_string(t)

    def backspaceCompare_const_space(self, s: str, t: str) -> bool:
        i = len(s) - 1
        j = len(t) - 1

        while True:
            i = get_next_char(s, i)
            j = get_next_char(t, j)

            if i < 0 and j < 0:
                return True

            if i <0 or j < 0 or s[i] != t[j]:
                return False

            i -= 1
            j -= 1



def test():
    s = 'ab#c'
    t = '#ac'
    sltn = Solution()
    assert sltn.backspaceCompare_const_space(s, t)


# def test_2():
#     s = 'ab##c'
#     t = '#ac'
#     sltn = Solution()
#     assert sltn.backspaceCompare_const_space(s, t) is False