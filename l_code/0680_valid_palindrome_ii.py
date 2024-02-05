# Time: O(n)  Space: O(n)
def valid_palindrome(s: str) -> bool:
    def is_valid(inp, i, j, skip):
        if i > j:
            return True
        if inp[i] == inp[j]:
            return is_valid(inp, i + 1, j - 1, skip)
        if skip:
            return is_valid(inp, i + 1, j, False) or is_valid(inp, i, j - 1, False)
        return False

    return is_valid(s, 0, len(s) - 1, True)


def test():
    assert valid_palindrome('aba')
    assert valid_palindrome('abca')
    assert valid_palindrome('abccdba')
    assert valid_palindrome('abxccdba') is False
    assert valid_palindrome('a')