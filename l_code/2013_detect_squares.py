import math
from collections import defaultdict


class Point:
    def __init__(self, pid, coords):
        self.pid = pid
        self.x = coords[0]
        self.y = coords[1]


class DetectSquares:
    def __init__(self):
        self.counter = 0
        self.points = []
        self.perp = defaultdict(list)

    def get_angle(self, mid_point, point2, point3):
        angle = abs(math.degrees(math.atan2(point2.y - mid_point.y, point2.x - mid_point.x) - math.atan2(point3.y - mid_point.y, point3.x - mid_point.x)))
        return angle if angle <= 180 else 360 - angle

    def add(self, point):
        point1 = Point(self.counter, point)
        self.counter += 1

        for i in range(len(self.points) - 1):
            point2 = self.points[i]
            for j in range(i+1, len(self.points)):
                point3 = self.points[j]
                if self.get_angle(point1, point2, point3) == 90:
                    self.perp[point1.pid].append((point2.pid, point3.pid))

        self.points.append(point1)

    def count(self, point):
        cur_point = Point(0, point)
        count = 0
        for mid_point_id, other_point_ids in self.perp.items():
            mid_point = self.points[mid_point_id]
            if mid_point.x == cur_point.x and mid_point.y == cur_point.y:
                continue
            for point_2_id, point_3_id in other_point_ids:
                point2 = self.points[point_2_id]
                point3 = self.points[point_3_id]

                if self.get_angle(cur_point, point3, point2) == 90:
                    count += 1
        return count


def test():
    ds = DetectSquares()
    ds.add([3, 10])
    ds.add([11, 2])
    ds.add([3, 2])
    assert ds.count([11, 10]) == 1