def eval_rpn(tokens):
    """
    :type tokens: List[str]
    :rtype: int
    """
    stack = []
    ops = '*/+-'

    for token in tokens:
        if token in ops:
            val_1 = stack.pop()
            val_2 = stack.pop()

            if token == '+':
                stack.append(val_1 + val_2)
            elif token == '-':
                stack.append(val_2 - val_1)
            elif token == '*':
                stack.append(val_1 * val_2)
            else:
                stack.append(int(val_2 / val_1))
        else:
            stack.append(int(token))

    return stack.pop()


def test_1():
    tokens = ['2', '3', '+']
    assert eval_rpn(tokens) == 5


def test_2():
    tokens = ["4", "13", "5", "/", "+"]
    assert eval_rpn(tokens) == 6


def test_3():
    tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    assert eval_rpn(tokens) == 22