import heapq
from operator import itemgetter


def binary_search(row):
    low = 0
    high = len(row)

    while low < high:
        mid = (low + high) // 2
        if row[mid] == 1:
            low = mid + 1
        else:
            high = mid

    return low


# Time: O(m*log(nk)) Space: O(k)
def k_weakest_rows_heap(mat, k):
    heap = []
    m = len(mat)
    n = len(mat[0])

    # O(m*log(n) + m*log(k)) = O(m*(log(n)+log(k))) = O(m*log(nk))
    for i in range(m):
        s = binary_search(mat[i])

        if len(heap) < k:
            heapq.heappush(heap, (-s, -i))
        elif heap[0][0] < -s:
            heapq.heappushpop(heap, (-s, -i))

    # O(k)
    res = []
    while heap:
        res.append(-heapq.heappop(heap)[1])

    return res[::-1]


# Using sorting
# Time: O(m*n + m*log(m))  Space: O(m + k)
def k_weakest_rows(mat, k):
    # mat is an m x n matrix
    rows = []

    # O(m*n)
    for i in range(len(mat)):
        s = 0
        for j in range(len(mat[i])):
            if mat[i][j] == 1:
                s += 1

        rows.append((s, i))

    # O(m*log(m))
    rows = sorted(rows, key=itemgetter(0))
    # rows.sort() does the same thing. This will sort firstly by s and secondly by i.

    # O(k)
    res = []
    for i in range(k):
        res.append(rows[i][1])

    return res


def test_1():
    mat = [[1, 1, 0, 0, 0],
           [1, 1, 1, 0, 0],
           [1, 1, 0, 0, 0],
           [1, 1, 0, 0, 0],
           [1, 1, 0, 0, 0]]
    k = 2
    assert k_weakest_rows_heap(mat, k) == [0, 2]