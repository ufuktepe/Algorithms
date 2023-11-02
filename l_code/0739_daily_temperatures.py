def daily_temperatures(temperatures):
    """
    :type temperatures: List[int]
    :rtype: List[int]
    """

    stack = []
    res = [0] * len(temperatures)

    for i in range(len(temperatures)):
        while stack:
            if temperatures[stack[-1]] < temperatures[i]:
                res[stack[-1]] = i - stack[-1]
                stack.pop()
            else:
                break

        stack.append(i)

    return res


def test_1_temperature():
    temperatures = [10]
    assert daily_temperatures(temperatures) == [0]


def test_increasing_2_temperatures():
    temperatures = [10, 12]
    assert daily_temperatures(temperatures) == [1, 0]


def test_decreasing_2_temperatures():
    temperatures = [14, 12]
    assert daily_temperatures(temperatures) == [0, 0]


def test_mixed_3_temperatures():
    temperatures = [10, 12, 8]
    assert daily_temperatures(temperatures) == [1, 0, 0]