import heapq


# Time: O(N*log(N)) Space: O(N)
def last_stone_weight(stones):
    heap = [-stone for stone in stones]  # O(N)
    heapq.heapify(heap)                  # O(N)

    # O(N*log(N))
    while len(heap) > 1:
        y = heapq.heappop(heap) * -1     # O(log(N))
        x = heapq.heappop(heap) * -1     # O(log(N))

        if x == y:
            continue

        heapq.heappush(heap, x - y)      # O(log(N))

    return 0 if len(heap) == 0 else heap[0] * -1


def test_1():
    stones = [10, 40, 20, 35]
    assert last_stone_weight(stones) == 5


def test_2():
    stones = [10, 10, 10, 10]
    assert last_stone_weight(stones) == 0