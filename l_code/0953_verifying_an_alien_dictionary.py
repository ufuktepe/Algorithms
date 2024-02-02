# Let n be the num of words and m be the max word length
# Time: O(n*m)  Space: O(1)
def isAlienSorted(words, order):
    char_idx = {}
    for idx, ch in enumerate(order):
        char_idx[ch] = idx

    for i in range(len(words) - 1):
        word1 = words[i]
        word2 = words[i + 1]

        for j in range(min(len(word1), len(word2))):
            if char_idx[word1[j]] < char_idx[word2[j]]:
                break
            elif char_idx[word1[j]] > char_idx[word2[j]]:
                return False
        else:
            if len(word1) > len(word2):
                return False

    return True


def test():
    words = ["hello", "leetcode"]
    order = "hlabcdefgijkmnopqrstuvwxyz"
    assert isAlienSorted(words, order)


def test_2():
    words = ["word","world","row"]
    order = "worldabcefghijkmnpqstuvxyz"
    assert isAlienSorted(words, order) is False


def test_3():
    words = ["apple","app"]
    order = "abcdefghijklmnopqrstuvwxyz"
    assert isAlienSorted(words, order) is False