from collections import deque, defaultdict


# Time: O(m+n)  Space: O(m+n)  where n is the num of buses and m is the num of bus stops
def min_transfers(routes, source, target):
    if source == target:
        return 0
    adj = defaultdict(set)            # maps buses to a set of adjacent buses
    stop_to_buses = defaultdict(set)  # maps bus stops to a set of buses
    bus_route = defaultdict(set)      # maps buses to bus_stops that they visit

    for bus, route in enumerate(routes):
        for bus_stop in route:
            bus_route[bus].add(bus_stop)
            stop_to_buses[bus_stop].add(bus)

    for bus, bus_stops in bus_route.items():
        for bus_stop in bus_stops:
            for other_bus in stop_to_buses[bus_stop]:
                if other_bus == bus:
                    continue
                adj[bus].add(other_bus)

    visited = set()  # busses we have been on

    q = deque()
    for bus in stop_to_buses[source]:
        q.append((bus, 1))
        visited.add(bus)

    while q:
        cur_bus, cur_count = q.popleft()

        if target in bus_route[cur_bus]:
            return cur_count

        for other_bus in adj[cur_bus]:
            if other_bus not in visited:
                visited.add(other_bus)
                q.append((other_bus, cur_count + 1))

    return -1


def test():
    routes = [[1, 2, 7], [3, 6, 7]]
    source = 1
    target = 6
    assert min_transfers(routes, source, target) == 2
