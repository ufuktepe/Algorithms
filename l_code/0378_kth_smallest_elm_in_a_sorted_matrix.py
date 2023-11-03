import heapq


# Time: O(k*log(k))  Space: O(k)
def kth_smallest_elm(mat, k):
    pq = [(mat[0][0], 0, 0)]   # O(1)
    n = len(mat)
    count = 0
    mat[0][0] = None           # O(1)

    # O(k*log(k))
    while pq:
        count += 1
        cur, i, j = heapq.heappop(pq)   # O(log(k))

        if count == k:
            return cur

        if j + 1 < n and mat[i][j + 1] is not None:
            heapq.heappush(pq, (mat[i][j + 1], i, j + 1))  # O(log(k))
            mat[i][j + 1] = None                           # I forgot to add this line in my first attempt
        if i + 1 < n and mat[i + 1][j] is not None:
            heapq.heappush(pq, (mat[i + 1][j], i + 1, j))  # O(log(k))
            mat[i + 1][j] = None                           # I forgot to add this line in my first attempt


def test_1():
    mat = [[-5]]
    k = 1
    assert kth_smallest_elm(mat, k) == -5


def test_2():
    mat = [[1, 2, 12],
           [3, 4, 15],
           [20, 21, 22]]

    k = 6
    assert kth_smallest_elm(mat, k) == 15