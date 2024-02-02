# Time: O(n)  Space: O(1)
def gas_station(gas, cost):
    i = j = 0
    n = len(gas)
    rem = 0
    covered = 0

    while i < n:
        if covered == n:
            return i

        if rem + gas[j] - cost[j] >= 0:
            rem = rem + gas[j] - cost[j]
            covered += 1
            j = (j + 1) % n
        elif covered == 0:
            i += 1
            j += 1
        else:
            while covered > 0:
                rem = rem - (gas[i] - cost[i])
                i += 1
                covered -= 1
                if i >= n:
                    return -1

    return -1


# Time: O(n)  Space: O(1)
def gas_station_v2(gas, cost):
    i = j = 0
    n = len(gas)
    rem = 0
    covered = 0

    while i < n:
        if covered == n:
            return i

        if rem + gas[j] - cost[j] >= 0:
            rem = rem + gas[j] - cost[j]
            covered += 1
            j = (j + 1) % n
        elif i >= j + 1:
            return -1
        else:
            rem = 0
            covered = 0
            i = j + 1
            j = j + 1

    return -1


def test():
    gas = [1, 2, 10]
    cost = [1, 3, 1]
    assert gas_station(gas, cost) == 2


def test_2():
    gas = [3, 5, 7, 9]
    cost = [1, 1, 1, 40]
    assert gas_station(gas, cost) == -1


def test_3():
    gas = [2, 3, 4]
    cost = [3, 4, 3]
    assert gas_station_v2(gas, cost) == -1