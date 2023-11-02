def get_adj(i, j, image):
    adj = []

    if i - 1 >= 0:
        adj.append((i - 1, j))

    if i + 1 < len(image):
        adj.append((i + 1, j))

    if j - 1 >= 0:
        adj.append((i, j - 1))

    if j + 1 < len(image[i]):
        adj.append((i, j + 1))

    return adj


def floodFill(image, sr, sc, color):
    """
    :type image: List[List[int]]
    :type sr: int
    :type sc: int
    :type color: int
    :rtype: List[List[int]]
    """
    stack = [(sr, sc)]
    orig_color = image[sr][sc]
    # visited = {(sr, sc)}

    while stack:
        x, y = stack.pop()

        image[x][y] = color

        for i, j in get_adj(x, y, image):
            # if (i, j) in visited:
            #     continue
            # visited.add((i, j))

            if image[i][j] == orig_color:
                stack.append((i, j))

    return image


def test_1():
    image = [[1, 1, 1],
             [1, 1, 0],
             [1, 0, 1]]
    sr = 1
    sc = 1
    color = 2
    assert floodFill(image, sr, sc, color) == [[2, 2, 2],
                                               [2, 2, 0],
                                               [2, 0, 1]]