from stack_array_based import Stack

def evaluate_expr(expr):
    stack_vals = Stack()
    stack_ops = Stack()

    # Supported operators
    ops = '+-*'

    lefty = '{(['
    righty = '})]'

    expr_items = expr.split(' ')

    for item in expr_items:
        if item in lefty:
            continue

        if item in righty:
            val_1 = stack_vals.pop()
            val_2 = stack_vals.pop()
            op = stack_ops.pop()

            val_output = compute(val_2, val_1, op)
            stack_vals.push(val_output)

        elif item in ops:
            stack_ops.push(item)

        else:
            stack_vals.push(item)

    if not stack_ops.is_empty():
        val_1 = stack_vals.pop()
        val_2 = stack_vals.pop()
        op = stack_ops.pop()

        val_output = compute(val_2, val_1, op)
        stack_vals.push(val_output)

    return stack_vals.top()


def compute(x, y, op):
    x = int(x)
    y = int(y)

    if op == '+':
        return x + y
    if op == '-':
        return x - y
    if op == '*':
        return x * y
    raise ValueError('invalid operator.')


expr = '( 5 + ( 2 * 3 ) ) * 2 '

print(evaluate_expr(expr))
