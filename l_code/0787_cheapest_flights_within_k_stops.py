from collections import defaultdict, deque


def cheapest_flights(n, flights, src, dst, k):
    adj = defaultdict(list)
    for i, j, price in flights:
        adj[i].append((price, j))

    cost = [float('inf')] * n
    cost[src] = 0

    q = deque([src])

    while k >= 0:
        k -= 1
        next_cost = cost[:]
        next_q = deque()
        added = set()
        while q:
            i = q.popleft()
            cur_cost = cost[i]
            for price, j in adj[i]:
                if j not in added:
                    next_q.append(j)
                    added.add(j)
                if next_cost[j] > cur_cost + price:
                    next_cost[j] = cur_cost + price
        q = next_q
        cost = next_cost

    return cost[dst] if cost[dst] < float('inf') else -1


# Time: O(k*(M+N))  Space: O(M+N)
def cheapest_flights_bellman_ford(n, flights, src, dst, k):
    adj = defaultdict(list)

    # O(M)
    for i, j, price in flights:
        adj[i].append((price, j))

    # O(N)
    cost = [float('inf')] * n
    cost[src] = 0

    # O(k*(M+N))
    while k >= 0:
        k -= 1
        # O(N)
        next_cost = cost[:]

        # O(M+N)
        for i in range(n):
            cur_cost = cost[i]
            for price, j in adj[i]:
                if next_cost[j] > cur_cost + price:
                    next_cost[j] = cur_cost + price
        cost = next_cost

    return cost[dst] if cost[dst] < float('inf') else -1

def test():
    flights = [[0, 1, 100], [0, 2, 200], [1, 2, 10], [1, 3, 300], [2, 3, 20]]
    n = 4
    src = 0
    dst = 3
    assert cheapest_flights_bellman_ford(n, flights, src, dst, k=1) == 220
    assert cheapest_flights_bellman_ford(n, flights, src, dst, k=2) == 130
