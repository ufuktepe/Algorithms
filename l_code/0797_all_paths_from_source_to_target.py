# Time: O(2^(N-2))  Space: O(N*2^(N-2)) = O(2^(N-1))
def all_paths_source_target(graph):
    n = len(graph)
    res = []

    def dfs(i, path):
        if i == n - 1:
            res.append(path[:])
            return

        for j in graph[i]:
            path.append(j)
            dfs(j, path)
            path.pop()

    dfs(0, [0])
    return res


def test():
    graph = [[1], []]
    assert all_paths_source_target(graph) == [[0, 1]]


def test_2():
    graph = [[1, 2, 3], [3], [3], []]
    assert all_paths_source_target(graph) == [[0, 1, 3], [0, 2, 3], [0, 3]]