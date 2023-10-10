def bfs_adj_list(s, adj_list):
    parent = [None for _ in adj_list]
    parent[s] = s
    level = [[s]]

    while level[-1]:
        level.append([])  # Create a new level
        for v in level[-2]:
            for neighbor in adj_list[v]:
                if parent[neighbor] is None:
                    parent[neighbor] = v
                    level[-1].append(neighbor)

    return parent


def unweighted_shortest_path(adj_list, s, t):
    parent = bfs_adj_list(s, adj_list)
    if parent[t] is None:
        return None
    path = [t]
    v = t
    while v != s:
        path.append(parent[v])
        v = parent[v]

    path.reverse()
    return path


if __name__ == '__main__':
    adj_list = [[5, 6],
                [3, 4, 6],
                [3, 5],
                [1, 2, 6],
                [1],
                [0, 2],
                [0, 1, 3]]

    print(unweighted_shortest_path(adj_list, 0, 4))