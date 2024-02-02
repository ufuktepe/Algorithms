def pacific_atlantic(heights):
    PACIFIC = 0b0100
    ATLANTIC = 0b1000
    FIRST_VISIT = 0b0001
    SECOND_VISIT = 0b0010
    BOTH = 0b1111

    m = len(heights)
    n = len(heights[0])

    access = [[0] * n for _ in range(m)]

    def visit(i, j, parent_access, visit_bit):
        access[i][j] |= parent_access | visit_bit

        for x, y in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            n_i, n_j = i + x, j + y
            if 0 <= n_i < m and 0 <= n_j < n and not (access[n_i][n_j] & visit_bit) and heights[i][j] <= heights[n_i][n_j]:
                visit(n_i, n_j, parent_access, visit_bit)

    # Visit from Pacific
    for j in range(n):
        if not (access[0][j] & FIRST_VISIT):
            visit(0, j, PACIFIC, FIRST_VISIT)
    for i in range(m):
        if not (access[i][0] & FIRST_VISIT):
            visit(i, 0, PACIFIC, FIRST_VISIT)

    # Visit from Atlantic
    for j in range(n):
        if not (access[n - 1][j] & SECOND_VISIT):
            visit(n - 1, j, ATLANTIC, SECOND_VISIT)
    for i in range(m):
        if not (access[i][m - 1] & SECOND_VISIT):
            visit(i, m - 1, ATLANTIC, SECOND_VISIT)

    res = []
    for i in range(m):
        for j in range(n):
            if access[i][j] == BOTH:
                res.append([i, j])

    return res


def test():
    heights = [[1, 2, 2, 3, 5],
               [3, 2, 3, 4, 4],
               [2, 4, 5, 3, 1],
               [6, 7, 1, 4, 5],
               [5, 1, 1, 2, 4]]

    assert pacific_atlantic(heights) == [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]