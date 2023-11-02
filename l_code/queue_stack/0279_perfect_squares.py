from collections import deque

# DP solution, exceeds time limit
def numSquares(n):
    res = [float('inf') for _ in range(n + 1)]
    res[1] = 1

    s = set()
    upper = int(n ** 0.5) + 1
    for i in range(1, upper):
        s.add(i ** 2)

    for i in range(2, n + 1):
        if i in s:
            res[i] = 1
        else:
            for j in range(1, i // 2 + 1):
                res[i] = min(res[i], res[i - j] + res[j])
    return res[n]


def numSquares_bfs(n):
    visited = set()
    q = deque([0])
    visited.add(0)
    count = 0

    while q:
        count += 1
        for _ in range(len(q)):
            cur = q.popleft()

            # Loop over its neighbors
            j = 1
            while j ** 2 <= n:
                neighbor = cur + j ** 2
                if neighbor == n:
                    return count
                if neighbor not in visited:
                    visited.add(neighbor)
                    q.append(neighbor)
                j += 1
    return -1


def test_1():
    assert numSquares_bfs(1) == 1


def test_2():
    assert numSquares_bfs(13) == 2


def test_3():
    assert numSquares_bfs(12) == 3