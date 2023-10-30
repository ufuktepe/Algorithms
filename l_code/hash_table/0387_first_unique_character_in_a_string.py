def first_uniq_char(s):
    """
    :type s: str
    :rtype: int
    """
    hashmap = {}

    for ch in s:
        if ch in hashmap:
            hashmap[ch] += 1
        else:
            hashmap[ch] = 1

    for i, ch in enumerate(s):
        if hashmap[ch] == 1:
            return i

    return -1


def test_success():
    s = 'lolipop'
    assert first_uniq_char(s) == 3


def test_failure():
    s = 'abababab'
    assert first_uniq_char(s) == -1