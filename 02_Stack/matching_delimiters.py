from stack_array_based import Stack


def is_matched(expr):
    lefty = '{(['
    righty = '})]'

    stack = Stack()

    for char in expr:
        if char in lefty:
            stack.push(char)
        elif char in righty:
            lefty_char = lefty[righty.index(char)]
            if stack.is_empty() or lefty_char != stack.pop():
                return False

    return stack.is_empty()


if __name__ == '__main__':
    expr = '[asd(sd)]'

    if is_matched(expr):
        print('Matched')
    else:
        print('Does not match')