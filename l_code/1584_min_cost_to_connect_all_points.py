# Let N be the num of points. Then, num of edges = N*(N-1)/2 = O(N^2)
# Time: O(N^2*log(N))  Space: O(N^2)
import heapq


def min_cost_kruskal(points):
    edges = []

    # O(N^2)
    for i in range(len(points) - 1):
        for j in range(i + 1, len(points)):
            dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
            edges.append((i, j, dist))

    # O(N^2*log(N))
    edges.sort(key=lambda item: item[2])

    roots = [i for i in range(len(points))]
    ranks = [0 for _ in range(len(points))]

    def find(x):
        if roots[x] != x:
            roots[x] = find(roots[x])
        return roots[x]

    def union(x, y):
        root_x = find(x)
        root_y = find(y)

        if root_x == root_y:
            return

        if ranks[root_x] > ranks[root_y]:
            roots[root_y] = root_x
        else:
            roots[root_x] = root_y
            if ranks[root_x] == ranks[root_y]:
                ranks[root_y] += 1

    total = 0
    n = 0
    # O(N*alpha(N))
    for i, j, dist in edges:
        if find(i) == find(j):
            continue

        union(i, j)
        total += dist
        n += 1

        if n == len(points) - 1:
            break

    return total


def min_cost_prim(points):
    n = len(points)
    count = 0
    heap = [(0, 0)] # (dist, index)
    total = 0
    in_mst = [False] * n

    # O(N^2*log(N))
    while count < n:
        # O(log(N))
        dist, i = heapq.heappop(heap)

        if in_mst[i]:
            continue

        in_mst[i] = True
        count += 1
        total += dist

        # Add edges to heap -> O(N*log(N))
        for j in range(n):
            if in_mst[j]:
                continue
            weight = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
            # O(log(N))
            heapq.heappush(heap, (weight, j))

    return total


def test():
    points = [[0, 0], [2, 3], [4, 5], [6, 8]]
    assert min_cost_prim(points) == 14

