def get_num_ways(board):
    if not board:
        return 0

    total_n = 0

    for j in board[0]:
        if not board[0][j]:
            new_board = [[cell for cell in row] for row in board[1:]]

            for i, row in enumerate(new_board):
                row[j] = True
                left = j - i - 1
                right = j + i + 1

                if left >= 0:
                    row[left] = True
                if right < len(row):
                    row[right] = True

            total_n += get_num_ways(new_board)

    return total_n




board = [[0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0]]
print(get_num_ways(board))

