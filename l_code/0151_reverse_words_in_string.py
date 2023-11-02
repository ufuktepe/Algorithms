def reverseWords(s):
    """
    :type s: str
    :rtype: str
    """
    words = [word.strip() for word in s.split(' ') if word.strip() != '']

    l, r = 0, len(words) - 1

    while l < r:
        words[l], words[r] = words[r], words[l]
        l += 1
        r -= 1

    return ' '.join(words)


def test_1_word_no_whitespace():
    s = 'car'
    assert reverseWords(s) == 'car'


def test_1_word_with_leading_whitespace():
    s = ' car'
    assert reverseWords(s) == 'car'


def test_1_word_with_trailing_whitespace():
    s = 'car '
    assert reverseWords(s) == 'car'


def test_2_words_no_whitespace():
    s = 'blue car'
    assert reverseWords(s) == 'car blue'


def test_2_words_with_leading_whitespace():
    s = ' blue car'
    assert reverseWords(s) == 'car blue'


def test_2_words_with_trailing_whitespace():
    s = 'blue car '
    assert reverseWords(s) == 'car blue'


def test_3_words_multiple_whitespace():
    s = 'a good   example'
    assert reverseWords(s) == 'example good a'