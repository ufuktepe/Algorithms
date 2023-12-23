# Time: O((M+N)*alpha(N))
# Space: O(N)
from collections import defaultdict


def find_components(n, edges):
    root = [i for i in range(n)]
    rank = [0 for _ in range(n)]

    def find(x):
        if root[x] != x:
            root[x] = find(root[x])
        return root[x]

    def union(x, y):
        root_x = find(x)
        root_y = find(y)

        if root_x == root_y:
            return

        if rank[root_x] > rank[root_y]:
            root[root_y] = root_x
        else:
            root[root_x] = root_y
            if rank[x] == rank[y]:
                rank[root_y] += 1

    for x, y in edges:
        union(x, y)

    comps = set()
    for i in range(n):
        comps.add(find(i))

    return len(comps)


# Time: O(M+N)
# Space: O(M+N)
def find_components_dfs(n, edges):
    adj = defaultdict(list)
    for x, y in edges:
        adj[x].append(y)
        adj[y].append(x)

    visited = set()

    def dfs(i):
        visited.add(i)
        for j in adj[i]:
            if j not in visited:
                dfs(j)
    count = 0
    for i in range(n):
        if i not in visited:
            dfs(i)
            count += 1

    return count


# Time: O(M+N)
# Space: O(M+N)
def find_components_dfs_iter(n, edges):
    adj = defaultdict(list)
    for x, y in edges:
        adj[x].append(y)
        adj[y].append(x)

    visited = set()
    count = 0
    for i in range(n):
        if i in visited:
            continue

        stack = [i]
        while stack:
            j = stack.pop()

            for k in adj[j]:
                if k not in visited:
                    visited.add(k)
                    stack.append(k)

        count += 1
    return count


def test():
    edges = [[0, 1]]
    n = 2
    assert find_components_dfs_iter(n, edges) == 1

    edges = [[0, 1]]
    n = 4
    assert find_components_dfs_iter(n, edges) == 3

    edges = [[0, 1], [1, 3]]
    n = 4
    assert find_components_dfs_iter(n, edges) == 2
