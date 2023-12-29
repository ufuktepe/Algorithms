def rotate_image(matrix):
    n = len(matrix)
    q = n - 1
    index = 0

    while q > 1:
        for r in range(q):
            i = index
            j = index + r
            prev = matrix[index][index + r]
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


