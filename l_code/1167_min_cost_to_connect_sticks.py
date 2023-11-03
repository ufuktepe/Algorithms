import heapq


# Time: O(N*log(N))  Space: O(1)
def connect_sticks(sticks):
    heapq.heapify(sticks)  # O(N)

    cost = 0

    # O(N*log(N))
    while len(sticks) > 1:
        z = heapq.heappop(sticks) + heapq.heappop(sticks)  # O(log(N))
        cost += z
        heapq.heappush(sticks, z)                          # O(log(N))

    return cost


def test_1():
    sticks = [10]
    assert connect_sticks(sticks) == 0


def test_2():
    sticks = [1, 2, 3, 5, 10]
    assert connect_sticks(sticks) == 41