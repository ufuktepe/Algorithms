def is_isomorphic(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    hashmap = {}
    seen = set()

    for i, ch in enumerate(s):
        if ch not in hashmap:
            if t[i] in seen:
                return False
            hashmap[ch] = t[i]
            seen.add(t[i])
        elif hashmap[ch] != t[i]:
            return False
    return True


def test_isomorphic():
    s = 'add'
    t = 'egg'
    assert is_isomorphic(s, t) == True


def test_not_isomorphic():
    s = 'egg'
    t = 'car'
    assert is_isomorphic(s, t) == False