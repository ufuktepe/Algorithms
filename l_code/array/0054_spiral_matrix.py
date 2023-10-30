

def spiral_matrix_rec(matrix, row_start, row_end, col_start, col_end, output=None):
    if output is None:
        output = []

    if row_end < row_start or col_end < col_start:
        return output

    # Get top row
    for j in range(col_start, col_end + 1):
        output.append(matrix[row_start][j])

    # Get right column
    for i in range(row_start + 1, row_end + 1):
        output.append(matrix[i][col_end])

    # Get bottom row
    if row_start != row_end:
        for j in range(col_end - 1, col_start - 1, -1):
            output.append(matrix[row_end][j])

    # Get left column
    if col_start != col_end:
        for i in range(row_end - 1, row_start, -1):
            output.append(matrix[i][col_start])

    row_start += 1
    row_end -= 1
    col_start += 1
    col_end -= 1

    return spiral_matrix_rec(matrix, row_start, row_end, col_start, col_end, output)


def spiral_matrix(matrix):
    if not matrix:
        return []

    row_start = 0
    row_end = len(matrix) - 1
    col_start = 0
    col_end = len(matrix[0]) - 1
    output = []

    while row_end >= row_start and col_end >= col_start:
        # Get top row
        for j in range(col_start, col_end + 1):
            output.append(matrix[row_start][j])

        # Get right column
        for i in range(row_start + 1, row_end + 1):
            output.append(matrix[i][col_end])

        # Get bottom row
        if row_start != row_end:
            for j in range(col_end - 1, col_start - 1, -1):
                output.append(matrix[row_end][j])

        # Get left column
        if col_start != col_end:
            for i in range(row_end - 1, row_start, -1):
                output.append(matrix[i][col_start])

        row_start += 1
        row_end -= 1
        col_start += 1
        col_end -= 1

    return output


def test_empty_matrix():
    assert spiral_matrix([]) == []


def test_1_by_1_matrix():
    input = [[3]]
    output = spiral_matrix(input)
    assert output == [3]


def test_1_by_2_matrix():
    input = [[1, 2]]
    assert spiral_matrix(input) == [1, 2]


def test_2_by_1_matrix():
    input = [[1], [2]]
    assert spiral_matrix(input) == [1, 2]


def test_2_by_2_matrix():
    input = [[1, 2], [3, 4]]
    assert spiral_matrix(input) == [1, 2, 4, 3]


def test_2_by_3_matrix():
    input = [[1, 2, 3], [4, 5, 6]]
    assert spiral_matrix(input) == [1, 2, 3, 6, 5, 4]


def test_3_by_2_matrix():
    input = [[1, 2], [4, 5], [7, 9]]
    assert spiral_matrix(input) == [1, 2, 5, 9, 7, 4]


if __name__ == '__main__':
    matrix = [[1, 2], [4, 5], [7, 9]]
    print(spiral_matrix_rec(matrix, row_start=0, row_end=len(matrix)-1, col_start=0, col_end=len(matrix[0])-1))