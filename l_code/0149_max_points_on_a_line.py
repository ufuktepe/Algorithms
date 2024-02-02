from collections import defaultdict


def max_points(points):
    if len(points) < 2:
        return len(points)
    s = defaultdict(set)  # maps (slope, intercept) to points
    point_groups = defaultdict(set)
    n = len(points)
    res = 0

    for i in range(n - 1):
        for j in range(i + 1, n):
            skip = False
            for group_i in point_groups[i]:
                if group_i in point_groups[j]:
                    skip = True
                    break

            if skip:
                continue

            if points[i][0] - points[j][0] == 0:
                s[('inf', points[i][0])].add(i)
                s[('inf', points[i][0])].add(j)
                point_groups[i].add(('inf', points[i][0]))
                point_groups[j].add(('inf', points[i][0]))

            else:
                slope = (points[i][1] - points[j][1]) / (points[i][0] - points[j][0])
                intercept = points[i][1] - slope * points[i][0]
                s[(slope, intercept)].add(i)
                s[(slope, intercept)].add(j)
                point_groups[i].add((slope, intercept))
                point_groups[j].add((slope, intercept))

    for group in s.values():
        res = max(res, len(group))

    return res

def test():
    points = [[1, 1], [4, 2], [2, 2], [3, 3], [2, 1]]
    assert max_points(points) == 3