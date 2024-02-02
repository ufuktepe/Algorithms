from collections import defaultdict


# Time: O(n!*n^2)  Space: O(n^2)
def n_queens(n):
    res = []

    def set_cell(board, row, col, occupied_cols, occupied_dia):
        board[row][col] = 'Q'
        occupied_cols.add(col)

        for count, i in enumerate(range(row + 1, len(board))):
            left_col = col - count - 1
            right_col = col + count + 1
            if left_col >= 0:
                occupied_dia[(i, left_col)] += 1
            if right_col < len(board):
                occupied_dia[(i, right_col)] += 1

    def remove_cell(board, row, col, occupied_cols, occupied_dia):
        board[row][col] = '.'
        occupied_cols.remove(col)

        for count, i in enumerate(range(row + 1, len(board))):
            left_col = col - count - 1
            right_col = col + count + 1
            if left_col >= 0:
                occupied_dia[(i, left_col)] -= 1
            if right_col < len(board):
                occupied_dia[(i, right_col)] -= 1

    def visit(board, row, col, occupied_cols, occupied_dia):
        set_cell(board, row, col, occupied_cols, occupied_dia)

        if row == len(board) - 1:
            res.append([''.join(r) for r in board])
            board[row][col] = '.'

        else:
            for j in range(len(board)):
                if j not in occupied_cols and occupied_dia[(row + 1, j)] == 0:
                    visit(board, row + 1, j, occupied_cols, occupied_dia)

        remove_cell(board, row, col, occupied_cols, occupied_dia)

    occupied_cols = set()
    occupied_dia = defaultdict(int)

    board = [['.'] * n for _ in range(n)]

    for j in range(len(board)):
        visit(board, 0, j, occupied_cols, occupied_dia)

    return res


def test():
    assert n_queens(4) == [[".Q..",
                            "...Q",
                            "Q...",
                            "..Q."],
                           ["..Q.",
                            "Q...",
                            "...Q",
                            ".Q.."]]