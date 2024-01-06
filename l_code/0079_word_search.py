# Time: O((m*n)^2)  Space: O(L)  where L is the length of the word
def word_search(board, word):
    m = len(board)
    n = len(board[0])

    visited = set()

    def get_adj(r, c):
        adj = []

        if r + 1 < m:
            adj.append((r + 1, c))

        if 0 <= r - 1:
            adj.append((r - 1, c))

        if c + 1 < n:
            adj.append((r, c + 1))

        if 0 <= c - 1:
            adj.append((r, c - 1))

        return adj

    def search(r, c, k=0):
        visited.add((r, c))

        if k == len(word) - 1:
            return True

        for n_r, n_c in get_adj(r, c):
            if board[n_r][n_c] == word[k + 1] and (n_r, n_c) not in visited:
                if search(n_r, n_c, k + 1):
                    return True

        visited.remove((r, c))

        return False

    for i in range(m):
        for j in range(n):
            if board[i][j] == word[0] and search(i, j):
                return True

    return False


# def test():
#     board = [['a', 'b', 'c'],
#              ['d', 'e', 'f'],
#              ['x', 'y', 'z']]
#
#     assert word_search(board, word='bef')
#     assert word_search(board, word='cfx') is False
#     assert word_search(board, word='xyebad')


def test_2():
    board = [["C", "A", "A"],
             ["A", "A", "A"],
             ["B", "C", "D"]]
    word = "AAB"
    assert word_search(board, word)