from collections import defaultdict


# Let N be the num of variables, M be the num of equations and Q be the num of queries
# Time: O(Q*(N+M))  Space: O(M+N+Q)
def calc_equation(equations, values, queries):
    adj = defaultdict(dict)

    # O(M)
    for (a, b), val in zip(equations, values):
        adj[a][b] = val
        adj[b][a] = 1.0 / val

    res = []
    visited = set()

    def dfs(ch, target, cur_result=1):
        visited.add(ch)

        for adj_ch, val in adj[ch].items():
            new_cur_result = cur_result * val
            if adj_ch == target:
                res.append(new_cur_result)
                return True
            if adj_ch not in visited:
                if dfs(adj_ch, target, new_cur_result):
                    return True
        return False

    # O(Q*(N+M))
    for a, b in queries:
        visited = set()
        if a not in adj or b not in adj:
            res.append(-1)
        else:
            if not dfs(a, b):
                res.append(-1)

    return res


def calc_equation_union_find(equations, values, queries):
    roots = {}
    ranks = {}
    for a, b in equations:
        roots[a] = [a, 1]
        roots[b] = [b, 1]
        ranks[a] = 0
        ranks[b] = 0

    def find(ch):
        parent_ch, val = roots[ch]
        if parent_ch != ch:
            root_ch, cum_val = find(parent_ch)
            roots[ch] = [root_ch, cum_val * val]
        return roots[ch]

    def union(x, y, val):
        root_x, x_val = find(x)
        root_y, y_val = find(y)

        if root_x == root_y:
            return

        if ranks[root_x] > ranks[root_y]:
            roots[root_y] = [root_x, x_val / (y_val * val)]
        else:
            roots[root_x] = [root_y, (y_val * val) / x_val]
            if ranks[root_x] == ranks[root_y]:
                ranks[root_y] += 1

    for (a, b), val in zip(equations, values):
        union(a, b, val)

    res = []
    for a, b in queries:
        if a not in roots or b not in roots:
            res.append(-1)
        else:
            root_a, a_val = find(a)
            root_b, b_val = find(b)
            if root_a == root_b:
                res.append(a_val / b_val)
            else:
                res.append(-1)

    return res


def test():
    equations = [["a", "b"], ["c", "d"]]
    values = [1, 1]
    queries = [["a", "c"], ["b", "d"], ["b", "a"], ["d", "c"]]
    assert calc_equation_union_find(equations, values, queries) == [-1, -1, 1, 1]