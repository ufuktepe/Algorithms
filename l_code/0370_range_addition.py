from collections import defaultdict


# Let n be length and m be length of updates
# Time: O(n+m)  Space: O(n)
def get_array(length, updates):
    arr = [0] * length
    idx_to_vals = defaultdict(int)
    val = 0

    for start, end, inc in updates:
        idx_to_vals[start] += inc
        idx_to_vals[end + 1] -= inc

    for i in range(length):
        val += idx_to_vals[i]
        arr[i] = val

    return arr


def test():
    length = 5
    updates = [[1, 3, 2], [2, 4, -1], [3, 4, 5]]
    assert get_array(length, updates) == [0, 2, 1, 6, 4]