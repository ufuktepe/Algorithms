# Others solution
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


# First attempt
def length_of_longest_substring(s):
    """
    :type s: str
    :rtype: int
    """
    letters = {}  # Maps letters to their indices
    i = j = 0
    best_i = best_j = None

    while j < len(s):
        if s[j] in letters:
            if best_i is None or (j - i) > (best_j - best_i + 1):
                best_i = i
                best_j = j - 1
            # Remove each letter from letters up to and including index letters[s[j]]
            new_i = letters[s[j]] + 1
            for k in range(i, new_i):
                del letters[s[k]]

            i = new_i
        letters[s[j]] = j
        j += 1

    if best_i is None or (j - i) > (best_j - best_i + 1):
        return j - i

    return best_j - best_i + 1


def test_empty_string():
    s = ''
    assert length_of_longest_substring(s) == 0


def test_length_1():
    s = 'aaaa'
    assert length_of_longest_substring(s) == 1


def test_length_2():
    s = 'aab'
    assert length_of_longest_substring(s) == 2


def test_length_3():
    s = 'abcabcbb'
    assert lengthOfLongestSubstring(s) == 3