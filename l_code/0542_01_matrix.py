from collections import deque


def get_adj(i, j, mat):
    adj = []

    if i - 1 >= 0:
        adj.append((i - 1, j))

    if i + 1 < len(mat):
        adj.append((i + 1, j))

    if j - 1 >= 0:
        adj.append((i, j - 1))

    if j + 1 < len(mat[i]):
        adj.append((i, j + 1))

    return adj

# First attempt
def update_matrix(mat):
    """
    :type mat: List[List[int]]
    :rtype: List[List[int]]
    """
    q = deque()
    dist = [[None for _ in range(len(mat[i]))] for i in range(len(mat))]

    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j] == 0:
                q.append((i, j))
                dist[i][j] = 0

    while q:
        i, j = q.popleft()

        for ni, nj in get_adj(i, j, mat):
            if dist[ni][nj] is None:
                dist[ni][nj] = dist[i][j] + 1
                q.append((ni, nj))

    return dist


def update_matrix_v2(mat):
    """
    :type mat: List[List[int]]
    :rtype: List[List[int]]
    """
    q = deque()
    adj = [0, 1, 0, -1, 0]
    m = len(mat)
    n = len(mat[0])

    for i in range(m):
        for j in range(n):
            if mat[i][j] == 0:
                q.append((i, j))
            else:
                mat[i][j] = -1  # Mark as not processed

    while q:
        i, j = q.popleft()

        for k in range(4):
            ni, nj = i + adj[k], j + adj[k + 1]
            if not (0 <= ni < m) or not (0 <= nj < n) or mat[ni][nj] != -1:
                continue
            mat[ni][nj] = mat[i][j] + 1
            q.append((ni, nj))
    return mat


def test_1():
    mat = [[0, 1, 1],
           [1, 1, 1],
           [1, 1, 0]]

    assert update_matrix_v2(mat) == [[0, 1, 2],
                                  [1, 2, 1],
                                  [2, 1, 0]]