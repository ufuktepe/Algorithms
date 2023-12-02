# This is from Leetcode editorial
def search_matrix(matrix, target):
    def search(top, bot, left, right):
        if top > bot or left > right:
            return False
        if not (matrix[top][left] <= target <= matrix[bot][right]):
            return False

        row = top
        col = (left + right) // 2

        # Find the row such that matrix[row-1][col] < target < matrix[row][col]
        for row in range(top, bot + 1):
            if matrix[row][col] == target:
                return True
            if target < matrix[row][col]:
                break

        # Search bottom left: row, bot, left, col - 1
        # Search top right: top, row, col + 1, right
        return search(row, bot, left, col - 1) or search(top, row, col + 1, right)

    return search(0, len(matrix) - 1, 0, len(matrix[0]) - 1)


# My solution
def search_matrix_v2(matrix, target):
    def search(top, bot, left, right):
        if top > bot or left > right:
            return False
        if not (matrix[top][left] <= target <= matrix[bot][right]):
            return False

        row = (top + bot) // 2
        col = (left + right) // 2

        if target == matrix[row][col]:
            return True

        if target < matrix[row][col]:
            # Discard bottom right
            # Search top left: top, row - 1, left, col - 1
            # Search top right: top, row - 1, col, right
            # Search bottom left: row, bot, left, col - 1
            top_left = search(top, row - 1, left, col - 1)
            top_right = search(top, row - 1, col, right)
            bot_left = search(row, bot, left, col - 1)
            return top_left or top_right or bot_left
        else:
            # Discard top left
            # Search top right: top, row, col + 1, right
            # Search bottom left: row + 1, bot, left, col
            # Search bottom right: row + 1, bot, col + 1, right
            top_right = search(top, row, col + 1, right)
            bot_left = search(row + 1, bot, left, col)
            bot_right = search(row + 1, bot, col + 1, right)
            return top_right or bot_left or bot_right

    return search(0, len(matrix) - 1, 0, len(matrix[0]) - 1)


def search_matrix_binary_search(matrix, target):
    def search(row, low, high):
        if low > high:
            return False

        mid = (low + high) // 2

        if target == row[mid]:
            return True

        if target < row[mid]:
            return search(row, low, mid - 1)
        else:
            return search(row, mid + 1, high)

    for row in matrix:
        if row[0] <= target and search(row, 0, len(row) - 1):
            return True
    return False


# Time: O(n+m)  Space: O(1)
def search_matrix_efficient(matrix, target):
    if not matrix:
        return False
    j = 0
    i = len(matrix) - 1
    while i >= 0 and j < len(matrix[0]):
        if matrix[i][j] == target:
            return True
        if matrix[i][j] > target:
            i -= 1
        else:
            j += 1

    return False



def test():
    matrix = [[1,4,7,11,15],
              [2,5,8,12,19],
              [3,6,9,16,22],
              [10,13,14,17,24],
              [18,21,23,26,30]]
    assert search_matrix_v2(matrix, 5) == True


def test_1_by_1():
    matrix = [[1]]
    assert search_matrix(matrix, 1) == True
    assert search_matrix(matrix, 2) == False


def test_1_by_3():
    matrix = [[1, 3, 5]]
    assert search_matrix(matrix, 5) == True
    assert search_matrix(matrix, 4) == False

def test_5_by_5():
    matrix = [[1, 2, 3, 4, 5],
              [6, 7, 8, 9, 10],
              [11, 12, ],
              [1, 2, 3, 4, 5],
              [1, 2, 3, 4, 5],]