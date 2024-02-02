# Time: O(n)  Space: O(1)
def removeInterval(intervals, toBeRemoved):
    res = []
    start_r, end_r = toBeRemoved
    for start, end in intervals:
        if start <= start_r < end:
            if start < start_r:
                res.append([start, start_r])
            if end_r < end:
                res.append([end_r, end])

        elif start_r < start < end_r:
            if end_r < end:
                res.append([end_r, end])

        else:
            res.append([start, end])
    return res


def test():
    intervals = [[0, 2], [3, 4], [5, 7]]
    toBeRemoved = [1, 6]
    assert removeInterval(intervals, toBeRemoved) == [[0, 1], [6, 7]]