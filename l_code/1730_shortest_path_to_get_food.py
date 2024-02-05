from collections import deque


# Time: O(n)  Space: O(n)
def get_food(grid):
    m, n = len(grid), len(grid[0])
    s = None

    for i in range(m):
        for j in range(n):
            if grid[i][j] == '*':
                s = (i, j, 0)
                break
        else:
            continue
        break

    q = deque([s])
    visited = {(s[0], s[1])}
    directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

    while q:
        i, j, dist = q.popleft()

        for x, y in directions:
            if 0 <= x + i < m and 0 <= y + j < n and grid[x + i][y + j] != 'X' and (x + i, y + j) not in visited:
                if grid[x + i][y + j] == '#':
                    return dist + 1
                visited.add((x + i, y + j))
                q.append((x + i, y + j, dist + 1))
    return -1


def test():
    grid = [["X","X","X","X","X","X","X","X"],
            ["X","*","O","X","O","#","O","X"],
            ["X","O","O","X","O","O","X","X"],
            ["X","O","O","O","O","#","O","X"],
            ["X","X","X","X","X","X","X","X"]]

    assert get_food(grid) == 6