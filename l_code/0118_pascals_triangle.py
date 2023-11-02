# Second attempt
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """

        currRowIndex = 0
        pre_row = None
        while currRowIndex <= rowIndex:
            row = [1] * (currRowIndex + 1)
            if currRowIndex > 1:
                for i in range(1, currRowIndex):
                    row[i] = pre_row[i - 1] + pre_row[i]
            pre_row = row
            currRowIndex += 1
        return row


# First attempt
def generate(numRows):
    """
    :type numRows: int
    :rtype: List[List[int]]
    """
    cur = 1
    output = []
    while cur <= numRows:
        local = []
        for i in range(cur):
            if i == 0 or i == cur - 1:
                local.append(1)
            else:
                local.append(output[-1][i - 1] + output[-1][i])
        output.append(local)
        cur += 1

    return output


def generate_v2(numRows):
    """ More Elegant. """
    output = [[1] * (i + 1) for i in range(numRows)]

    for i in range(numRows):
        for j in range(1, i):
            output[i][j] = output[i - 1][j - 1] + output[i - 1][j]

    return output


def test_1_row():
    assert generate_v2(1) == [[1]]


def test_2_rows():
    assert generate_v2(2) == [[1], [1, 1]]


def test_3_rows():
    assert generate_v2(3) == [[1], [1, 1], [1, 2, 1]]


def test_5_rows():
    assert generate_v2(5) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]