# Time: O(log(n))  Space: O(1)
def is_power_of_three(n):
    x = 0

    while 3 ** x < n:
        x += 1

    return 3 ** x == n

def test():
    assert is_power_of_three(0) is False
    assert is_power_of_three(-1) is False
    assert is_power_of_three(-3) is False
    assert is_power_of_three(2) is False
    assert is_power_of_three(4) is False
    assert is_power_of_three(12) is False
    assert is_power_of_three(1)
    assert is_power_of_three(3)
    assert is_power_of_three(9)
