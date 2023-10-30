def is_valid_sudoku(board):
    """
    :type board: List[List[str]]
    :rtype: bool
    """
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    groups = [[set() for _ in range(3)] for _ in range(3)]

    for i, cells in enumerate(board):
        for j, cell in enumerate(cells):
            if cell == '.':
                continue
            x = i // 3
            y = j // 3
            if cell in rows[i] or cell in cols[j] or cell in groups[x][y]:
                return False
            rows[i].add(cell)
            cols[j].add(cell)
            groups[x][y].add(cell)
    return True


def test_success():
    board = [["5","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]
    assert is_valid_sudoku(board) == True


def test_failure():
    board = [["8","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]
    assert is_valid_sudoku(board) == False