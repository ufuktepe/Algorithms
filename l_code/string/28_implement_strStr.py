# KMP solution
def strStr2(s, p):
    n, m = len(s), len(p)
    if n == 0 or m == 0:
        return -1

    i = j = 0

    lps = build_lps(p)

    while i < n:
        if s[i] == p[j]:
            i += 1
            j += 1
        else:
            if i != 0 and j != 0:
                j = lps[j - 1]
            else:
                i += 1
        if j == m:
            return i - j
    return -1


def build_lps(p):
    lps = [0] * len(p)  # lps[i] is the length of the longest prefix suffix considering chars up to including p[i]
    i = 1
    length = 0          # length of the previous longest prefix suffix

    while i < len(p):
        if p[i] == p[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps


# Naive solution
def strStr(haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    if needle == '':
        return -1

    for i in range(len(haystack) - len(needle) + 1):
        for j in range(len(needle)):
            if haystack[i + j] != needle[j]:
                break
            if j == len(needle) - 1:
                return i

    return -1


def test_successful_find_long_haystack():
    haystack = 'abcdefgh'
    needle = 'ef'
    assert strStr2(haystack, needle) == 4


def test_unsuccessful_find_long_haystack():
    haystack = 'abcdefgh'
    needle = 'zrr'
    assert strStr2(haystack, needle) == -1


def test_successful_find_equal_length_haystack_needle():
    haystack = 'abcd'
    needle = 'abcd'
    assert strStr2(haystack, needle) == 0


def test_unsuccessful_find_equal_length_haystack_needle():
    haystack = 'abcd'
    needle = 'abcz'
    assert strStr2(haystack, needle) == -1


def test_unsuccessful_find_zero_length_needle():
    haystack = 'abcd'
    needle = ''
    assert strStr2(haystack, needle) == -1


if __name__ == '__main__':
    needle = 'aabaabc'
    haystack = 'aabxaabayaabaabc'
    print(strStr2(haystack, needle))