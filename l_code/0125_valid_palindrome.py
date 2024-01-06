# Time: O(n)  Space: O(n)
def isPalindrome(s):
    # O(n)
    chars = [ch.lower() for ch in s if ch.isalnum()]

    # O(n)
    chars_reversed = chars[::-1]

    # O(n)
    for a, b in zip(chars, chars_reversed):
        if a != b:
            return False

    return True


def test():
    s = 'aabbaa'
    assert isPalindrome(s) == True


def test_2():
    s = 'aa, b, baa'
    assert isPalindrome(s) == True


def test_3():
    s = 'a'
    assert isPalindrome(s) == True


def test_4():
    s = ' '
    assert isPalindrome(s) == True