# Time: O(n)  Space: O(n)
def kth_grammar_rec(n, k):
    # Base case
    if n == 1:
        return 0

    half_elms = 2 ** (n - 2)

    if k <= half_elms:
        return kth_grammar_rec(n - 1, k)
    else:
        return (kth_grammar_rec(n - 1, k - half_elms) + 1) % 2


# Time: O(n)  Space: O(1)
def kth_grammar_iter(n, k):
    res = 1  # Initial guess

    for i in range(n, 1, -1):
        half_elms = 2 ** (i - 2)
        if k > half_elms:
            k -= half_elms
            res = (res + 1) % 2

    if res == 0:
        # Initial guess was correct
        return 1
    else:
        # Initial guess was incorrect
        return 0


def test_rec():
    assert kth_grammar_rec(1, 1) == 0
    assert kth_grammar_rec(2, 2) == 1
    assert kth_grammar_rec(3, 2) == 1
    assert kth_grammar_rec(4, 4) == 0


def test_iterc():
    assert kth_grammar_iter(1, 1) == 0
    assert kth_grammar_iter(2, 2) == 1
    assert kth_grammar_iter(3, 2) == 1
    assert kth_grammar_iter(4, 4) == 0