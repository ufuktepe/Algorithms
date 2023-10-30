

def reverse_string(s, start_idx=0):
    end_idx = len(s) - start_idx - 1
    if start_idx < end_idx:
        s[start_idx], s[end_idx] = s[end_idx], s[start_idx]
        reverse_string(s, start_idx + 1)


def test_string_of_length_1():
    s = ['a']
    reverse_string(s)
    assert s[0] == 'a'


def test_string_of_length_2():
    s = ['a', 'b']
    reversed = [item for item in s[::-1]]
    reverse_string(s)
    assert s == reversed


def test_string_of_length_3():
    s = ['a', 'b', 'c']
    reversed = [item for item in s[::-1]]
    reverse_string(s)
    assert s == reversed