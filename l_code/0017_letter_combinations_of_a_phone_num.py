# Time: O(4^n)  Space:
def letter_combinations(digits):
    if not digits:
        return

    letter_map = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
    res = []

    def calc_combinations(prefix, i=0):
        if i == len(digits):
            res.append(''.join(prefix))
            return

        for ch in letter_map[digits[i]]:
            prefix.append(ch)
            calc_combinations(prefix, i + 1)
            prefix.pop()

    calc_combinations([])
    return res


def test():
    assert letter_combinations('23') == ["ad","ae","af","bd","be","bf","cd","ce","cf"]