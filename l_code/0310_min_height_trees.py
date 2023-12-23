from collections import defaultdict


def find_min_height_tree(n, edges):
    degree = [0 for _ in range(n)]
    nodes = {i for i in range(n)}
    adj = defaultdict(set)
    for a, b in edges:
        adj[a].add(b)
        adj[b].add(a)
        degree[a] += 1
        degree[b] += 1

    q = []

    for node, children in adj.items():
        if len(children) == 1:
            q.append(node)

    while len(nodes) > 2:
        next_q = []
        for node in q:
            nodes.remove(node)

            for adj_node in adj[node]:
                degree[adj_node] -= 1
                if degree[adj_node] == 1:
                    next_q.append(adj_node)

        q = next_q

    return list(nodes)


def test():
    edges = [[0,1],[0,2],[0,3],[3,4],[4,5]]
    n = 6
    assert find_min_height_tree(n, edges) == [3]