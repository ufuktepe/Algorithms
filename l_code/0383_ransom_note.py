from collections import Counter


# Let n be the length of ransomNote and m be the length of magazine
# Time: O(m + n)  Space: O(m)
def can_construct(ransomNote, magazine):
    letterCounts = Counter(magazine)  # O(m)

    # O(n)
    for ch in ransomNote:
        if ch not in letterCounts or letterCounts[ch] == 0:
            return False
        letterCounts[ch] -= 1

    return True


def test():
    assert can_construct('abc', 'abc')
    assert can_construct('abc', 'abcd')
    assert can_construct('abc', 'adc') is False