def rotate_image(matrix):
    n = len(matrix)
    q = n - 1
    index = 0

    while q > 0:
        for r in range(q):
            i = index
            j = index + r
            prev = matrix[i][j]
            for k in range(4):
                temp = matrix[j][n - 1 - i]
                matrix[j][n - 1 - i] = prev
                prev = temp

                i, j = j, n - 1 - i

        index += 1
        q -= 2


def test():
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]
    rotate_image(matrix)
    assert matrix == [[7, 4, 1],
                      [8, 5, 2],
                      [9, 6, 3]]


def test_2():
    matrix = [[1, 2, 3, 4, 5],
              [6, 7, 8, 9, 10],
              [11, 12, 13, 14, 15],
              [16, 17, 18, 19, 20],
              [21, 22, 23, 24, 25]]
    rotate_image(matrix)
    assert matrix == [[21, 16, 11, 6, 1],
                      [22, 17, 12, 7, 2],
                      [23, 18, 13, 8, 3],
                      [24, 19, 14, 9, 4],
                      [25, 20, 15, 10, 5]]


