class Vertex:
    def __init__(self, item):
        self.item = item
        self.parent = None
        self.adj = []
        self.visit_start = None
        self.visit_end = None


def visit(vertex, time):
    time += 1
    vertex.visit_start = time
    for u in vertex.adj:
        if u.visit_start is None:
            u.parent = vertex
            time = visit(u, time)
    time += 1
    vertex.visit_end = time
    return time


def dfs(vertices):
    time = 0
    for vertex in vertices:
        if vertex.visit_start is None:
            visit(vertex, time)


if __name__ == '__main__':
    v = Vertex('v')
    r = Vertex('r')
    s = Vertex('s')
    w = Vertex('w')
    t = Vertex('t')

    v.adj = [r, w]
    r.adj = [s, v]
    s.adj = [r, w]
    w.adj = [s, t, v]
    t.adj = [w]

    vertices = [r, v, w, s, t]

    dfs(vertices)

    for vertex in vertices:
        if vertex.parent:
            print(f'{vertex.item}: {vertex.visit_start} {vertex.visit_end} {vertex.parent.item}')
        else:
            print(f'{vertex.item}: {vertex.visit_start} {vertex.visit_end}')
