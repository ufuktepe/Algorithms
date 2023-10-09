class Vertex:
    def __init__(self, item):
        self.item = item
        self.parent = None
        self.adj = []             # List of tuples (vertex, weight), where weight is the edge weight
        self.dist = float('inf')  # Distance to source


def visit(vertex, rev_top_order):
    for item in vertex.adj:
        adj_vertex, _ = item

        if adj_vertex.parent is None:
            adj_vertex.parent = vertex
            rev_top_order = visit(adj_vertex, rev_top_order)

    rev_top_order.append(vertex)
    return rev_top_order


def dfs(s):
    s.parent = s
    order = visit(s, [])
    order.reverse()
    return order


def dag_compute_shortest_dist(s):
    topological_order = dfs(s)
    s.dist = 0
    for u in topological_order:
        for item in u.adj:
            v, weight = item
            if v.dist > u.dist + weight:
                v.dist = u.dist + weight
                v.parent = u


def get_path(source, dest):
    path = []
    curr_vertex = dest
    while True:
        path.append(curr_vertex)
        # check if source is found
        if curr_vertex is source:
            break
        # Check if root is found
        if curr_vertex == curr_vertex.parent:
            return None
        curr_vertex = curr_vertex.parent

    path.reverse()
    return path


if __name__ == '__main__':
    a = Vertex('a')
    b = Vertex('b')
    c = Vertex('c')
    d = Vertex('d')
    e = Vertex('e')

    vertices = [a, b, c, d, e]

    a.adj = [(b, 1), (d, 5)]
    b.adj = [(e, 1)]
    d.adj = [(c, 2)]
    e.adj = [(c, 4), (d, 1)]

    dag_compute_shortest_dist(a)

    for v in vertices:
        print(f'{v.item} {v.dist}')

    source = d
    dest = a
    print(f'Path from {source.item} to {dest.item}')
    path = get_path(source, dest)
    if not path:
        print('No path exists')
    else:
        for v in path:
            print(v.item)
