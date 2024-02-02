from collections import  deque


class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:

        @lru_cache(maxsize=None)
        def dfs(x, y):
            if x + y == 0:
                # base case: (0, 0)
                return 0
            elif x + y == 2:
                # base case: (1, 1), (0, 2), (2, 0)
                return 2
            else:
                return min(dfs(abs(x - 1), abs(y - 2)), dfs(abs(x - 2), abs(y - 1))) + 1

        return dfs(abs(x), abs(y))


# Time: O(max(x, y)^2)  Space: O(max(x, y)^2)
def minKnightMoves(x: int, y: int) -> int:
    q = deque([(0, 0, 0)])
    moves = ((-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1))
    visited = set()

    while q:
        i, j, dist = q.popleft()
        if i == x and j == y:
            return dist

        for m, n in moves:
            a = i + m
            b = j + n
            if (a, b) in visited:
                continue
            visited.add((a, b))
            q.append((a, b, dist + 1))


def test():
    assert minKnightMoves(1, 2) == 1
    assert minKnightMoves(0, 0) == 0
    assert minKnightMoves(3, 3) == 2