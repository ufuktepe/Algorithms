# Time: O(M*log(M) + N + M*alpha(N)) where N is the num of nodes and M is the num of logs
# Space: O(N+M)   Python uses Timesort whose space complexity to sort M items is O(M)
def earliest_acq(logs, n):
    logs.sort(key=lambda item: item[0])

    root = [i for i in range(n)]
    rank = [0 for _ in range(n)]

    def find(x):
        if root[x] != x:
            root[x] = find(root[x])
        return root[x]

    def union(x, y):
        root_x = find(x)
        root_y = find(y)

        if root_x == root_y:
            return False

        if rank[root_x] > rank[root_y]:
            root[root_y] = root_x
        else:
            root[root_x] = root_y
            if rank[root_x] == rank[root_y]:
                rank[root_y] += 1
        return True

    count = n

    for timestamp, x, y in logs:
        if union(x, y):
            count -= 1
            if count == 1:
                return timestamp
    return -1


def test_1():
    logs = [[5, 0, 1]]
    n = 2
    assert earliest_acq(logs, n) == 5


def test_2():
    logs = [[5, 0, 1]]
    n = 3
    assert earliest_acq(logs, n) == -1


def test_3():
    logs = [[5, 0, 1], [2, 2, 3], [9, 0, 2], [91, 0, 3]]
    n = 4
    assert earliest_acq(logs, n) == 9