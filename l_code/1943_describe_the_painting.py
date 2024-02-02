# Time: O(n*log(n))  Space: O(n)
def split(segments):
    res = []
    points = []

    # O(n)
    for start, end, val in segments:
        points.append((start, 1, val))
        points.append((end, 0, val))

    # O(n*log(n))
    points.sort()
    active = 0
    total_val = 0
    last_x = None

    # O(n)
    for x, pos, val in points:
        if pos == 1:
            if active > 0 and last_x != x:
                res.append([last_x, x, total_val])
            active += 1
            last_x = x
            total_val += val
        else:
            if last_x != x:
                res.append([last_x, x, total_val])
            active -= 1
            last_x = x if active > 0 else None
            total_val -= val

    return res


def test():
    segments = [[1, 4, 1], [4, 5, 2]]
    assert split(segments) == [[1, 4, 1], [4, 5, 2]]