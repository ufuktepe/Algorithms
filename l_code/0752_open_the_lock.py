from collections import deque


def openLock(deadends, target):
    """
    :type deadends: List[str]
    :type target: str
    :rtype: int
    """
    q = deque()
    q.append('0000')
    dist = {'0000': 0}
    deadends = set(deadends)
    if target == '0000':
        return 0
    if '0000' in deadends:
        return -1

    while q:
        cur = q.popleft()

        for neighbor in get_neighbors(cur, deadends):
            if neighbor == target:
                return dist[cur] + 1
            if neighbor not in dist:
                dist[neighbor] = dist[cur] + 1
                q.append(neighbor)
    return -1


def get_neighbors(comb, deadends):
    neighbors = []
    for i in range(4):
        digit = int(comb[i])
        neighbor_1 = comb[:i] + str((digit + 1) % 10) + comb[i + 1:]
        neighbor_2 = comb[:i] + str((digit - 1) % 10) + comb[i + 1:]

        if neighbor_1 not in deadends:
            neighbors.append(neighbor_1)
        if neighbor_2 not in deadends:
            neighbors.append(neighbor_2)

    return neighbors


def test_success():
    deadends = ['0001', '0010', '0100', '9000', '0900', '0090', '0009']
    assert openLock(deadends, '2110') == 4


def test_failure():
    deadends = ['0000']
    assert openLock(deadends, '8888') == -1