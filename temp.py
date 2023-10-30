# def len_of_longest_substring(s):
#     i = j = 0
#     n = 0
#     hmap = {}  # maps letters to indices
#
#     while j < len(s):
#         if s[j] not in hmap or i > hmap[s[j]]:
#             n = max(n, j - i + 1)
#         else:
#             i = hmap[s[j]] + 1
#
#         hmap[s[j]] = j
#         j += 1
#
#     return n


def len_of_longest_substring(s):
    i = 0
    j = 1
    n = 0
    hmap = {}  # maps letters to indices

    while j <= len(s):
        if s[j] not in hmap or i > hmap[s[j]]:
            n = max(n, j - i + 1)
        else:
            i = hmap[s[j]] + 1

        hmap[s[j]] = j
        j += 1

    return n


def length_of_longest_substring_v2(s):
    start = maxLength = 0
    usedChar = {}

    for i in range(len(s)):
        if s[i] in usedChar and start <= usedChar[s[i]]:
            start = usedChar[s[i]] + 1
        else:
            maxLength = max(maxLength, i - start + 1)

        usedChar[s[i]] = i

    return maxLength


def test_length_1():
    s = 'aaaaa'
    assert len_of_longest_substring(s) == 1


def test_length_2():
    s = 'aabaa'
    assert len_of_longest_substring(s) == 2


def test_length_3():
    s = 'xzzab'
    assert len_of_longest_substring(s) == 3


def test_length_3_v2():
    s = 'abcabcbb'
    assert len_of_longest_substring(s) == 3