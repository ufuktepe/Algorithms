
def treasureship(board):
    n = len(board[0])

    # s[i] is the max score using the first i columns
    s = [None for _ in range(n + 1)]

    # s_top[i] is the max score using the first i columns and board[0][i - 1] is empty
    s_top = [None for _ in range(n + 1)]

    # s_bot[i] is the max score using the first i columns and board[1][i - 1] is empty
    s_bot = [None for _ in range(n + 1)]

    # Base cases
    s[0] = 0
    s[1] = board[0][0] + board[1][0]
    s_top[0] = s_top[1] = 0
    s_bot[0] = s_bot[1] = 0

    for i in range(2, n + 1):
        j = i - 1                           # Index for the board
        v = board[0][j] + board[1][j]       # Place vertically
        h1 = board[0][j] + board[0][j - 1]  # Place horizontally on 1st row
        h2 = board[1][j] + board[1][j - 1]  # Place horizontally on 2nd row

        s[i] = max(s[i - 1], (s[i - 1] + v), (s_top[i - 1] + v), (s_bot[i - 1] + v))
        s_top[i] = max(s_top[i - 1], s_bot[i - 1] + h2, s[i - 2] + h2)
        s_bot[i] = max(s_bot[i - 1], s_top[i - 1] + h1, s[i - 2] + h1)

    return s


if __name__ == '__main__':
    board = [[10, -5, -20, 25, 40],
             [20, 15, -35, -5, -5]]

    print(treasureship(board))