from collections import Counter


# Let n be max(len(s), len(t))
# Time: O(n)  Space:
def valid_anagram(s, t):
    if len(s) != len(t):
        return False

    s_map = Counter(s)
    t_map = Counter(t)

    for ch, freq in s_map.items():
        if ch not in t_map or t_map[ch] != freq:
            return False

    return True


def test():
    s = 'abcdefg'
    t = 'fgebcad'
    assert valid_anagram(s, t)


def test_2():
    s = 'abcdefg'
    t = 'fgebcaa'
    assert valid_anagram(s, t) is False


def test_3():
    s = 'abcdefg'
    t = 'fgebca'
    assert valid_anagram(s, t) is False


def test_4():
    s = 'abcdefg!'
    t = 'f!gebcad'
    assert valid_anagram(s, t)