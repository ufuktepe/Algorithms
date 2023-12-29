def rotate_image(matrix):
    n = len(matrix)

    layers = n // 2

    start = 0
    end = n - 1

    for layer in range(layers):
        j = layer
        for i in range(start, end + 1):
            matrix[j][n - i - 1] = matrix[i][j]


        start += 1
        end -= 1



