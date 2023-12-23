# Time: O(N+M)  Space: O(M+N)
def valid_path(n, edges, source, destination):
    adj = [[] for _ in range(n)]
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)

    visited = set()

    def dfs(i):
        if i == destination:
            return True
        visited.add(i)
        for j in adj[i]:
            if j not in visited:
                if dfs(j):
                    return True
        return False

    return dfs(source)


def test_2_nodes_failure():
    n = 2
    edges = []
    assert valid_path(n, edges, 0, 1) == False


def test_2_nodes_success():
    n = 2
    edges = [[0, 1]]
    assert valid_path(n, edges, 0, 1) == True


def test_3_nodes_failure():
    n = 3
    edges = [[0, 1]]
    assert valid_path(n, edges, 0, 2) == False

def test_3_nodes_success():
    n = 3
    edges = [[0, 1], [2, 1]]
    assert valid_path(n, edges, 0, 2) == True