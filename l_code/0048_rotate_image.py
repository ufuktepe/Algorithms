def rotate(matrix):
    n = len(matrix)

    left, right = 0, n - 1

    while left < right:
        for i in range(left, right):
            temp = matrix[n - i - 1][left]
            matrix[n - i - 1][left] = matrix[n - left - 1][n - i - 1]
            matrix[n - left - 1][n - i - 1] = matrix[i][n - left - 1]
            matrix[i][n - left - 1] = matrix[left][i]
            matrix[left][i] = temp

        left += 1
        right -= 1


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
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
    matrix = [[1, 2],
              [3, 4]]
    rotate(matrix)
    assert matrix == [[3, 1],
                      [4, 2]]


def test_2():
    matrix = [[1, 2, 3],
              [3, 4, 5],
              [6, 7, 8]]
    rotate(matrix)
    assert matrix == [[6, 3, 1],
                      [7, 4, 2],
                      [8, 5, 3]]