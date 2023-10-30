from collections import defaultdict


def get_key(str):
    letters = [c for c in str]
    letters.sort()
    return ''.join(letters)


def group_anagrams(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    d = defaultdict(list)

    for str in strs:
        k = get_key(str)
        d[k].append(str)

    output = []
    for strings in d.values():
        group = [s for s in strings]
        output.append(group)

    return output


def test_1_group():
    strs = ['abc']
    assert group_anagrams(strs) == [['abc']]


def test_2_groups():
    strs = ['abc', 'cab', 'ddd']
    assert group_anagrams(strs) == [['abc', 'cab'], ['ddd']]