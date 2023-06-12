from stack_array_based import Stack


def test_push():
    stack = Stack()
    stack.push(5)
    stack.push(3)

    assert stack.top() == 3


def test_pop():
    stack = Stack()
    stack.push(5)
    stack.push(3)

    assert stack.pop() == 3


def test_pop_empty_stack():
    stack = Stack()
    stack.push(5)
    stack.pop()

    assert stack.pop() is None
