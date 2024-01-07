# Time: O(n)  Space: O(1)
def convert_to_int(s):
    symbols = {'I': 1,
               'V': 5,
               'X': 10,
               'L': 50,
               'C': 100,
               'D': 500,
               'M': 1000,
               'IV': 4,
               'IX': 9,
               'XL': 40,
               'XC': 90,
               'CD': 400,
               'CM': 900}

    n = len(s)
    i = 0
    res = 0

    while i < n:
        single = s[i]
        double = s[i:i+2]

        if i == n - 1 or double not in symbols:
            res += symbols[single]
            i += 1
        else:
            res += symbols[double]
            i += 2

    return res


def test():
    assert convert_to_int('I') == 1
    assert convert_to_int('II') == 2
    assert convert_to_int('III') == 3
    assert convert_to_int('IV') == 4
    assert convert_to_int('XIV') == 14