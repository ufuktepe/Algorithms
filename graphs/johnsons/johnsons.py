from graphs.dijkstra.min_priority_queue import Item, MinPriorityQueue
from graphs.dijkstra.dijkstra import dijkstra
from graphs.bellman_ford.bellman_ford import bellman_ford


class Vertex(Item):
    def __init__(self, label):
        super().__init__(label=label, key=float('inf'))
        self.parent = None
        self.adj = []

    @property
    def dist(self):
        return self.key

    @dist.setter
    def dist(self, val):
        self.key = val


def get_new_graph(vertices):
    new_vertices = [v for v in vertices]

    # Create a source vertex
    s = Vertex('s')
    s.parent = s
    s.dist = 0

    # Add 0-weight edges from s to every other vertex
    for v in vertices:
        s.adj.append([v, 0])

    new_vertices.append(s)
    return new_vertices


def reweight_edges(h, vertices):
    for vertex in vertices:
        for item in vertex.adj:
            # Adjust the weight
            adj_vertex = item[0]
            item[1] = item[1] + h[vertex.label] - h[adj_vertex.label]


def reset_graph(s, vertices):
    for vertex in vertices:
        vertex.parent = None
        vertex.dist = float('inf')

    s.parent = s
    s.dist = 0


def johnsons(vertices):
    # Create the new graph
    new_vertices = get_new_graph(vertices)

    if not bellman_ford(new_vertices):
        # Graph has negative cycle
        return

    h = {vertex.label: vertex.dist for vertex in new_vertices}

    reweight_edges(h, new_vertices)

    output_table = {}  # {u.label: {v.label: dist}}

    for u in new_vertices:
        reset_graph(u, new_vertices)
        dijkstra(u, new_vertices)

        output_table[u.label] = {}
        for v in new_vertices:
            output_table[u.label][v.label] = v.dist - h[u.label] + h[v.label]

    return output_table


if __name__ == '__main__':
    a = Vertex('a')
    b = Vertex('b')
    c = Vertex('c')
    d = Vertex('d')
    e = Vertex('e')

    a.adj = [[b, 3], [c, 8], [e, -4]]
    b.adj = [[e, 7], [d, 1]]
    c.adj = [[b, 4]]
    d.adj = [[c, -5], [a, 2]]
    e.adj = [[d, 6]]

    vertices = [a, b, c, d, e]
    output_table = johnsons(vertices)

    for u, table in output_table.items():
        for v, dist in table.items():
            print(f'{u} - {v}: {dist}')
