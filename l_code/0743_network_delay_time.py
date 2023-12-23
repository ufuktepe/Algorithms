from collections import defaultdict
import heapq


# Time: O(N + M*log(N))  Space: O(N + M)
def network_delay_time(n, k, times):
    adj = defaultdict(list)

    # O(M)
    for i, j, weight in times:
        adj[i-1].append((j-1, weight))

    # O(N)
    dist = [float('inf')] * n
    dist[k-1] = 0
    count = 0

    pq = [(0, k-1)]  # dist and index
    visited = [False] * n

    while pq and count < n:
        cur_dist, cur_node = heapq.heappop(pq)

        if visited[cur_node]:
            continue
        visited[cur_node] = True
        count += 1

        for next_node, weight in adj[cur_node]:
            if dist[next_node] > weight + cur_dist:
                dist[next_node] = weight + cur_dist
                heapq.heappush(pq, (dist[next_node], next_node))

    if count != n:
        return -1
    return max(dist)


def test():
    times = [[2, 1, 30], [2, 3, 10], [3, 4, 40]]
    n = 4
    k = 2
    assert network_delay_time(n, k, times) == 50

def test():
    times = [[2, 1, 30], [2, 3, 10], [3, 4, 40]]
    n = 5
    k = 2
    assert network_delay_time(n, k, times) == -1