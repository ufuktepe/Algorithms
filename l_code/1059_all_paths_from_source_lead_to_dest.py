from collections import defaultdict


def leads_to_dest(n, edges, source, destination):
    adj = defaultdict(list)
    for a, b in edges:
        if a == b:
            continue
        adj[a].append([b, 0])  # second item = is_used

    def dfs(node, found):
        next_items = adj[node]

        has_child = False

        for next_item in next_items:
            next_node, is_used = next_item
            if is_used:
                continue
            has_child = True
            next_item[1] = 1
            found = dfs(next_node, found)
            if not found:
                return found
            next_item[1] = 0

        if not has_child:
            if node == destination:
                found = True
            else:
                found = False

        return found

    return dfs(source, False)


def test():
    n = 2
    edges = [[0, 1]]
    source = 0
    destination = 1
    assert leads_to_dest(n, edges, source, destination)


def test_2():
    n = 2
    edges = [[0, 1], [0, 1]]
    source = 0
    destination = 1
    assert leads_to_dest(n, edges, source, destination)


def test_3():
    n = 2
    edges = [[0, 1], [0, 1], [1, 0]]
    source = 0
    destination = 1
    assert leads_to_dest(n, edges, source, destination)


def test_4():
    n = 2
    edges = [[0, 1], [0, 2]]
    source = 0
    destination = 2
    assert leads_to_dest(n, edges, source, destination) == False


def test_5():
    n = 2
    edges = [[0, 1], [1, 9], [0, 2], [2, 9]]
    source = 0
    destination = 9
    assert leads_to_dest(n, edges, source, destination) == True