from collections import defaultdict

# Let N be the string length and M be the num of pairs
# Time: O(N + M + Nlog(N))
# Space: O(N + M)
def smallest_string_with_swaps(s, pairs):
    res = [ch for ch in s]

    adj = defaultdict(list)

    for i, j in pairs:
        adj[i].append(j)
        adj[j].append(i)

    visited = set()

    def dfs(i, letters, indices):
        visited.add(i)
        letters.append(s[i])
        indices.append(i)

        for j in adj[i]:
            if j not in visited:
                letters, indices = dfs(j, letters, indices)

        return letters, indices

    for i in range(len(s)):
        if i not in visited:
            letters, indices = dfs(i, [], [])   # N + M
            letters.sort()   # Nlog(N)
            indices.sort()   # Nlog(N)

            for ch, idx in zip(letters, indices):
                res[idx] = ch

    return ''.join(res)


def smallest_string_with_swaps_union_find(s, pairs):
    # O(N)
    roots = [i for i in range(len(s))]
    ranks = [0 for _ in s]

    def find(x):
        if roots[x] != x:
            roots[x] = find(roots[x])
        return roots[x]

    def union(x, y):
        root_x = find(x)
        root_y = find(y)

        if root_x == root_y:
            return

        if ranks[root_x] > ranks[root_y]:
            roots[root_y] = root_x
        else:
            roots[root_x] = root_y
            if ranks[root_x] == ranks[root_y]:
                ranks[root_y] += 1

    # O(M*alpha(N))
    for x, y in pairs:
        union(x, y)

    indices = defaultdict(list)
    letters = defaultdict(list)

    # O(N*alpha(N))
    for i, ch in enumerate(s):
        root = find(i)
        letters[root].append(ch)
        indices[root].append(i)

    # O(N)
    res = [ch for ch in s]

    # O(N*log(N))
    for roots, chars in letters.items():
        chars.sort()
        cur_indices = indices[roots]
        cur_indices.sort()

        for idx, ch in zip(cur_indices, chars):
            res[idx] = ch

    return ''.join(res)


def test():
    s = 'dcab'
    pairs = [[0, 3], [1, 2]]
    assert smallest_string_with_swaps_union_find(s, pairs) == "bacd"


def test_2():
    s = 'dcab'
    pairs = [[0,3],[1,2],[0,2]]
    assert smallest_string_with_swaps_union_find(s, pairs) == "abcd"
