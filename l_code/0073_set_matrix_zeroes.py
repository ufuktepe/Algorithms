# Time: O(n*m)  Space: O(1)
def set_matrix_zeroes(matrix):
    m, n = len(matrix), len(matrix[0])
    set_first_row, set_first_col = False, False

    for r in range(m):
        if matrix[r][0] == 0:
            set_first_col = True
            break

    for c in range(n):
        if matrix[0][c] == 0:
            set_first_row = True
            break

    for r in range(1, m):
        for c in range(1, n):
            if matrix[r][c] == 0:
                matrix[r][0] = 0
                matrix[0][c] = 0

    for r in range(1, m):
        for c in range(1, n):
            if matrix[r][0] == 0 or matrix[0][c] == 0:
                matrix[r][c] = 0

    if set_first_row:
        for i in range(n):
            matrix[0][i] = 0

    if set_first_col:
        for i in range(m):
            matrix[i][0] = 0


def test():
    matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    set_matrix_zeroes(matrix)
    assert matrix == [[0,0,0,0],[0,4,5,0],[0,3,1,0]]


def test_2():
    matrix = [[0, 1, 2],
              [3, 4, 5],
              [1, 3, 1]]
    set_matrix_zeroes(matrix)
    assert matrix == [[0, 0, 0],
                      [0, 4, 5],
                      [0, 3, 1]]