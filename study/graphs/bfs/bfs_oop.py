from collections import deque


class Vertex:
    def __init__(self, item):
        self.item = item
        self.parent = None
        self.dist = None
        self.adj = []


def bfs(s):
    frontier = deque()
    frontier.append(s)
    s.dist = 0

    while frontier:
        u = frontier.popleft()
        for v in u.adj:
            if v.dist is None:
                v.parent = u
                v.dist = v.parent.dist + 1
                frontier.append(v)


if __name__ == '__main__':
    v = Vertex('v')
    r = Vertex('r')
    s = Vertex('s')
    w = Vertex('w')
    t = Vertex('t')
    u = Vertex('u')
    x = Vertex('x')
    y = Vertex('y')

    v.adj = [r]
    r.adj = [s, v]
    s.adj = [r, w]
    w.adj = [s, x, t]
    t.adj = [w, x, u]
    x.adj = [w, t, y, u]
    u.adj = [t, x, y]
    y.adj = [x, u]

    bfs(s)
    x = 5



