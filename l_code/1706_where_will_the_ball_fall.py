# Time: O(m x n)  Space: O(1)
def find_ball(grid):
    m = len(grid)
    n = len(grid[0])

    def get_column(i):
        c = i
        for r in range(m):
            if grid[r][c] == 1:
                if c + 1 == len(grid[0]) or grid[r][c + 1] == -1:
                    return -1
                c += 1
            else:
                if c - 1 < 0 or grid[r][c - 1] == 1:
                    return -1
                c -= 1
        return c

    answer = []
    for i in range(n):
        answer.append(get_column(i))

    return answer


def test():
    grid = [[1, 1, 1, -1, -1], [1, 1, 1, -1, -1], [-1, -1, -1, 1, 1], [1, 1, 1, 1, -1], [-1, -1, -1, -1, -1]]
    assert find_ball(grid) == [1,-1,-1,-1,-1]