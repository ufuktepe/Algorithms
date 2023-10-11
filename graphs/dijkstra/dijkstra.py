from graphs.dijkstra.min_priority_queue import Item
from graphs.dijkstra.min_priority_queue import MinPriorityQueue


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


def dijkstra(s, vertices):
    s.parent = s
    s.dist = 0
    pq = MinPriorityQueue()
    for vertex in vertices:
        pq.insert(vertex)

    while not pq.is_empty():
        u = pq.extract_min()
        if not u.adj:
            continue

        for v, weight in u.adj:
            if v.dist > u.dist + weight:
                pq.decrease_key(v, u.dist + weight)
                v.parent = u


if __name__ == '__main__':
    s = Vertex('s')
    t = Vertex('t')
    y = Vertex('y')
    x = Vertex('x')
    z = Vertex('z')

    s.adj = [(t, 10), (y, 5)]
    t.adj = [(x, 1), (y, 2)]
    y.adj = [(t, 3), (z, 2), (x, 9)]
    z.adj = [(s, 7), (x, 6)]
    x.adj = [(z, 4)]

    vertices = [x, y, z, t, s]

    dijkstra(s, vertices)

    for vertex in vertices:
        print(f'{vertex.label} {vertex.dist} {vertex.parent.label}')
