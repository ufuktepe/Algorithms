def generate_parentheses(n):
    if n == 0:
        return ['']

    combinations = []
    for left in range(n):
        right = n - 1 - left

        for left_comb in generate_parentheses(left):
            for right_comb in generate_parentheses(right):
                combinations.append('(' + left_comb + ')' + right_comb)
    return set(combinations)


def test():
    assert set(generate_parentheses(2)) == {'()()', '(())'}
    assert set(generate_parentheses(3)) == {'()()()', '()(())', '(())()', '((()))', '(()())'}