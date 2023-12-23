from collections import defaultdict


def reconstruct_itinerary(tickets):
    adj = defaultdict(list)
    n_tickets = len(tickets)

    for a, b in tickets:
        adj[a].append([b, 0])  # second variable = is_used

    for airport in adj:
        adj[airport].sort(key=lambda item: item[0])

    path = ['JFK']

    def dfs(airport):
        for item in adj[airport]:
            next_airport, is_used = item
            if is_used:
                continue
            item[1] = 1
            path.append(next_airport)
            if len(path) == n_tickets + 1:
                return True

            if dfs(next_airport):
                return True

            item[1] = 0
            path.pop()

        return False

    dfs('JFK')

    return path

def reconstruct_itinerary_euler(tickets):
    adj = defaultdict(list)

    for origin, dest in tickets:
        adj[origin].append(dest)

    for origin, destinations in adj.items():
        destinations.sort(reverse=True)

    path = []

    def dfs(origin):
        next_airports = adj[origin]

        while next_airports:
            next_airport = next_airports.pop()
            dfs(next_airport)

        path.append(origin)

    dfs('JFK')

    return path[::-1]


def test():
    tickets = [['JFK', 'k'], ['JFK', 'n'], ['n', 'JFK']]
    assert reconstruct_itinerary_euler(tickets) == ['JFK', 'n', 'JFK', 'k']


def test_2():
    tickets = [['JFK', 'b'], ['b', 'c'], ['c', 'b'], ['JFK', 'c'], ['c', 'JFK']]
    assert reconstruct_itinerary_euler(tickets) == ['JFK', 'b', 'c', 'JFK', 'c', 'b']