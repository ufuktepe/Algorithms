# Time: O(N^2)  Space: O(N) where N is the number of nodes
def find_num_of_provinces(isConnected):
    n = len(isConnected)
    root = [i for i in range(n)]
    rank = [0 for i in range(n)]

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
            if rank[root_x] == rank[root_y]:
                rank[root_x] += 1

    # O(N^2)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if isConnected[i][j]:
                union(i, j)

    roots = set()
    for i in range(n):
        roots.add(find(i))

    return len(roots)


# Time: O(N^2)  Space: O(N)
def find_num_of_provinces_dfs(isConnected):
    n = len(isConnected)
    visited = [0 for _ in range(n)]

    def dfs(i):
        visited[i] = 1

        for j in range(n):
            if isConnected[i][j] and not visited[j]:
                dfs(j)

    n_provinces = 0

    for i in range(n):
        if not visited[i]:
            dfs(i)
            n_provinces += 1

    return n_provinces


def test():
    isConnected = [[1, 0, 0, 1, 1],
                   [0, 1, 1, 0, 0],
                   [0, 1, 1, 0, 0],
                   [1, 0, 0, 1, 0],
                   [1, 0, 0, 0, 1]]

    assert find_num_of_provinces_dfs(isConnected) == 2