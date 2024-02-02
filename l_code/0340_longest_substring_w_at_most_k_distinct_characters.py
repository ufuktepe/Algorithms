from collections import defaultdict


# Time: O(n)  Space: O(n)  where n is the length of s
def longest(s, k):
    if k == 0:
        return 0

    chars = defaultdict(int)
    max_len = 0
    i = j = 0
    num_of_distinct_chars = 0

    while j < len(s):
        cur_char = s[j]
        chars[cur_char] += 1

        if chars[cur_char] == 1:
            num_of_distinct_chars += 1

        while num_of_distinct_chars > k:
            chars[s[i]] -= 1
            if chars[s[i]] == 0:
                num_of_distinct_chars -= 1
            i += 1

        max_len = max(max_len, j - i + 1)

        j += 1

    return max_len


def test():
    s = 'abaacd'
    k = 2
    assert longest(s, k) == 4


def test_2():
    s = 'aabcdedd'
    k = 2
    assert longest(s, k) == 4


def test_3():
    s = 'abcd'
    k = 0
    assert longest(s, k) == 0

def test_4():
    s = 'abcdccaaa'
    k = 1
    assert longest(s, k) == 3