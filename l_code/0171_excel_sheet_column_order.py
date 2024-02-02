# Time: O(n)  Space: O(1)  where n is the length of columnTitle
def title_to_number(columnTitle):
    offset = 64

    res = 0

    for i, ch in enumerate(columnTitle[::-1]):
        res += (ord(ch) - offset) * 26 ** i

    return res


def test():
    assert title_to_number('A') == 1
    assert title_to_number('B') == 2
    assert title_to_number('Z') == 26
    assert title_to_number('AB') == 28