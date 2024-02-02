# Time: O(n)  Space: O(n)
def solve(board):
    m = len(board)
    n = len(board[0])
    if m < 3 or n < 3:
        return board

    visited = [[False] * n for _ in range(m)]
    directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

    def visit(r, c):
        visited[r][c] = True

        for x, y in directions:
            adj_r = x + r
            adj_c = y + c
            if 0 <= adj_r < m and 0 <= adj_c < n and board[adj_r][adj_c] == 'O' and not visited[adj_r][adj_c]:
                visit(adj_r, adj_c)

    # Top and bottom rows
    for j in range(n):
        for i in [0, m - 1]:
            if board[i][j] == 'O' and not visited[i][j]:
                visit(i, j)

    # Left and right columns
    for i in range(m):
        for j in [0, n - 1]:
            if board[i][j] == 'O' and not visited[i][j]:
                visit(i, j)

    for i in range(1, m - 1):
        for j in range(1, n - 1):
            if board[i][j] == 'O' and not visited[i][j]:
                board[i][j] = 'X'


def test():
    board = [['X', 'X', 'X', 'X', 'X'],
             ['X', 'X', 'O', 'O', 'X'],
             ['X', 'X', 'X', 'O', 'X'],
             ['X', 'O', 'X', 'X', 'X'],
             ['X', 'O', 'X', 'X', 'X']]
    solve(board)
    assert board == [['X', 'X', 'X', 'X', 'X'],
                     ['X', 'X', 'X', 'X', 'X'],
                     ['X', 'X', 'X', 'X', 'X'],
                     ['X', 'O', 'X', 'X', 'X'],
                     ['X', 'O', 'X', 'X', 'X']]


def test_2():
    board = [['X', 'X', 'O', 'X', 'O'],
             ['X', 'X', 'O', 'O', 'O'],
             ['X', 'X', 'X', 'O', 'X'],
             ['X', 'X', 'O', 'X', 'X'],
             ['X', 'O', 'X', 'X', 'X']]
    solve(board)
    assert board == [['X', 'X', 'O', 'X', 'O'],
                     ['X', 'X', 'O', 'O', 'O'],
                     ['X', 'X', 'X', 'O', 'X'],
                     ['X', 'X', 'X', 'X', 'X'],
                     ['X', 'O', 'X', 'X', 'X']]