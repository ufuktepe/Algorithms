class NumMatrix:

    def __init__(self, matrix):
        self.n_rows = len(matrix)
        self.n_cols = len(matrix[0])
        self.matrix = matrix

        self.row_sums = [[0] * self.n_cols for _ in range(self.n_rows)]

        for i in range(self.n_rows):
            running_sum = 0
            for j in range(self.n_cols):
                running_sum += matrix[i][j]
                self.row_sums[i][j] = running_sum

    # O(n) where n is the num of columns
    def update(self, row, col, val):
        for i in range(col, self.n_cols):
            self.row_sums[row][i] += val - self.matrix[row][col]
        self.matrix[row][col] = val

    # O(m) where m is the num of rows
    def sumRegion(self, row1, col1, row2, col2):
        """Returns the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2)."""
        region_sum = 0

        for r in range(row1, row2 + 1):
            region_sum += self.row_sums[r][col2]
            if col1 != 0:
                region_sum -= self.row_sums[r][col1 - 1]

        return region_sum


def test():
    matrix = [[2, 2, 2],
              [3, 3, 3],
              [4, 4, 4]]

    num_matrix = NumMatrix(matrix)
    num_matrix.update(1, 1, 10)
    assert num_matrix.sumRegion(1, 1, 2, 2) == 21