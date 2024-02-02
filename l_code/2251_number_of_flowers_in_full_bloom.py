# Let n be the num of flowers and m be the num of people
import heapq


# Time: O((n + m)*log(n + m))  Space: O(n + m)
def full_bloom(flowers, people):
    events = []
    # O(n)
    for start, end in flowers:
        events.append((start, 'f', 1))
        events.append((end + 1, 'f', -1))

    # O(m)
    for i, t in enumerate(people):
        events.append((t, 'p', i))

    # O((n + m) * log(n + m))
    events.sort()

    # O(m)
    res = [None] * len(people)
    count = 0

    # O(n + m)
    for t, entity, i in events:
        if entity == 'f':
            count += i
        else:
            res[i] = count

    return res


def full_bloom_v2(flowers, people):
    ppl_idx = [(t, j) for j, t in enumerate(people)]
    ppl_idx.sort()
    flowers.sort()
    pq = []
    i = 0
    res = [None] * len(people)

    for t, j in ppl_idx:
        while i < len(flowers) and flowers[i][0] <= t:
            heapq.heappush(pq, flowers[i][1])
            i += 1

        while pq and pq[0] < t:
            heapq.heappop(pq)

        res[j] = len(pq)

    return res


def test():
    flowers = [[1, 15], [5, 15], [3, 9], [7, 11], [12, 14]]
    people = [7, 11, 15]
    assert full_bloom_v2(flowers, people) == [4, 3, 2]


def test_2():
    flowers = [[1, 10], [3, 3]]
    people = [3, 3, 2]
    assert full_bloom_v2(flowers, people) == [2, 2, 1]