

class Vertex:
    def __init__(self, item):
        self.item = item
        self.parent = None
        self.visit_start = False
        self.visit_end = False
        self.adj = []


def visit(vertex):
    vertex.visit_start = True
    for neighbor in vertex.adj:
        if neighbor.visit_end:
            continue
        if neighbor.visit_start:
            return [vertex, neighbor]
        else:
            neighbor.parent = vertex
            return visit(neighbor)
    vertex.visit_end = True
    return None


def detect_cycle(vertices):
    for vertex in vertices:
        if not vertex.visit_start:
            v = visit(vertex)
            if v is not None:
                print_cycle(v[0], v[1])

def print_cycle(vertex, neighbor):
    cycle = [vertex]
    curr_vertex = vertex

    while curr_vertex.item != neighbor.item:
        curr_vertex = curr_vertex.parent
        cycle.append(curr_vertex)

    for v in cycle[::-1]:
        print(v.item)




if __name__ == '__main__':
    a = Vertex('a')
    b = Vertex('b')
    c = Vertex('c')
    d = Vertex('d')
    e = Vertex('e')

    a.adj = [c, b]
    b.adj = [c, d]
    c.adj = []
    d.adj = [e]
    e.adj = [b]

    detect_cycle([a, b, c, d, e])

