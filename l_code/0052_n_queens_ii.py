def total_n_queens(n):
    init_board = [[False for j in range(n)] for i in range(n)]

    def count_ways(board):

        total_n = 0

        if len(board) == 1:
            for cell in board[0]:
                if not cell:
                    total_n += 1
            return total_n

        for j in range(len(board[0])):
            if not board[0][j]:
                new_board = [[cell for cell in row] for row in board[1:]]

                for i, row in enumerate(new_board):
                    row[j] = True
                    left_dia = j - i - 1
                    right_dia = j + i + 1

                    if left_dia >= 0:
                        row[left_dia] = True
                    if right_dia < len(row):
                        row[right_dia] = True

                total_n += count_ways(new_board)

        return total_n

    return count_ways(init_board)


def test():
    assert total_n_queens(4) == 2