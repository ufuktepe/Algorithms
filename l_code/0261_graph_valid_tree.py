# Time: O(M*alpha(N)) where M is the num of edges and N is the num of nodes
# Space: O(N)
from collections import defaultdict


def is_valid_tree(n, edges):
    if n - 1 != len(edges):
        return False

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
            return False

        if rank[root_x] > rank[root_y]:
            root[root_y] = root_x
        else:
            root[root_x] = root_y
            if rank[root_x] == rank[root_y]:
                rank[root_y] += 1

        return True

    for x, y in edges:
        if not union(x, y):
            return False

    return True

# Time: O(M+N)
# Space: O(M+N)
def is_valid_tree_dfs(n, edges):
    if n - 1 != len(edges):
        return False

    adj = defaultdict(list)

    for x, y in edges:
        adj[x].append(y)
        adj[y].append(x)

    visited = [0 for _ in range(n)]

    def dfs(i, parent=None):
        visited[i] = 1

        for j in adj[i]:
            if j == parent:
                continue
            if visited[j]:
                return False
            return dfs(j, i)

        return True

    for i in range(n):
        if not visited[i]:
            if not dfs(i):
                return False

    return True



def test():
    edges = []
    n = 2
    assert is_valid_tree_dfs(n, edges) == False

    edges = [[0, 1]]
    assert is_valid_tree_dfs(n, edges) == True

    edges = [[0, 1], [1, 2], [2, 0]]
    n = 3
    assert is_valid_tree_dfs(n, edges) == False

    edges = [[0, 1], [1, 2]]
    n = 3
    assert is_valid_tree_dfs(n, edges) == True
