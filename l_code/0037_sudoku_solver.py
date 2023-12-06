def solve_sudoku(board):
    def get_next_cell_pos(i, j):
        if j == 8:
            i += 1
            j = 0
        else:
            j += 1
        return i, j

    def solve(board, rows, cols, boxes, i, j):
        if i == 9:
            return True

        if board[i][j] != '.':
            i, j = get_next_cell_pos(i, j)
            return solve(board, rows, cols, boxes, i, j)

        for num in range(1, 10):
            if num not in rows[i] and num not in cols[j] and num not in boxes[i // 3][j // 3]:
                board[i][j] = str(num)
                rows[i].add(num)
                cols[j].add(num)
                boxes[i // 3][j // 3].add(num)

                new_i, new_j = get_next_cell_pos(i, j)
                success = solve(board, rows, cols, boxes, new_i, new_j)

                if not success:
                    board[i][j] = '.'
                    rows[i].remove(num)
                    cols[j].remove(num)
                    boxes[i // 3][j // 3].remove(num)
                else:
                    return success
        return False

    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [[set() for j in range(3)] for i in range(3)]
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] != '.':
                cell = int(board[i][j])
                rows[i].add(cell)
                cols[j].add(cell)
                boxes[i // 3][j // 3].add(cell)

    solve(board, rows, cols, boxes, 0, 0)