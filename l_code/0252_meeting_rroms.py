# Time: O(n*log(n))  Space: O(1)
def can_attend(intervals):
    intervals.sort(key=lambda item: item[0])

    for i in range(len(intervals) - 1):
        if intervals[i + 1][0] < intervals[i][1]:
            return False

    return True


def test():
    intervals = [[1, 5], [6, 10]]
    assert can_attend(intervals)


def test_2():
    intervals = [[1, 5], [7, 10], [4, 6]]
    assert can_attend(intervals) is False