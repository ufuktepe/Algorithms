# Let n be the length of s, m be the num of words in wordDict and k be the largest word size in wordDict
# Time: O(n^3 + m*k)  Space: O(n + m*k)
def segment(s, wordDict):
    # O(m*k)
    wordDict = set(wordDict)
    n = len(s)

    dp = [False for _ in range(n + 1)]

    dp[0] = True

    # O(n^3)
    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in wordDict:
                dp[i] = True
                break

    return dp[n]


def test():
    s = 'carapple'
    wordDict = ['apple', 'car']
    assert segment(s, wordDict) == True


def test_2():
    s = 'carsapple'
    wordDict = ['apple', 'car']
    assert segment(s, wordDict) == False


def test_3():
    s = 'abcdefg'
    wordDict = ['a', 'bcd', 'defg']
    assert segment(s, wordDict) == False


def test_4():
    s = 'abcdefg'
    wordDict = ['a', 'bc', 'defg']
    assert segment(s, wordDict) == True


def test_5():
    s = 'c'
    wordDict = ['a', 'c', 'defg']
    assert segment(s, wordDict) == True