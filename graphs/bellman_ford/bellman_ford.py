

class Vertex:
    def __init__(self, item):
        self.item = item
        self.dist = float('inf')
        self.parent = None
        self.adj = []


def relax(u, v, weight):
    if v.dist > u.dist + weight:
        v.dist = u.dist + weight
        v.parent = u


def print_negative_cycle(u):
    cycle = [u]
    curr_vertex = u
    while True:
        if curr_vertex.parent is u:
            break
        if curr_vertex.parent is curr_vertex:
            print('No Negative Cycle exists.')
            return
        curr_vertex = curr_vertex.parent
        cycle.append(curr_vertex)

    print('Negative Cycle Exists!')
    cycle.reverse()
    for vertex in cycle:
        print(f'{vertex.item} -> ', end='')
    print(cycle[0].item)


def bellman_ford(vertices):
    for i in range(len(vertices) - 1):
        for vertex in vertices:
            for item in vertex.adj:
                adj_vertex, weight = item
                relax(vertex, adj_vertex, weight)
    for vertex in vertices:
        for item in vertex.adj:
            adj_vertex, weight = item
            if adj_vertex.dist > vertex.dist + weight:
                print_negative_cycle(adj_vertex)
                return False
    return True


if __name__ == '__main__':
    s = Vertex('s')
    t = Vertex('t')
    y = Vertex('y')
    x = Vertex('x')
    z = Vertex('z')

    s.adj = [(t, 1)]
    t.adj = [(y, -7)]
    y.adj = [(s, 6), (z, 1)]
    x.adj = [(t, 3)]
    z.adj = [(x, 2)]

    s.parent = s
    s.dist = 0

    vertices = [x, y, z, s, t]

    bellman_ford(vertices)

    for v in vertices:
        print(f'{v.item}: dist: {v.dist} parent: {v.parent.item}')
