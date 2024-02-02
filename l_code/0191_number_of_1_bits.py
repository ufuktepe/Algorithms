# Time: O(log(n))  Space: O(1)
def one_bits(n):
    count = 0
    while n:
        count += n & 1
        n = n >> 1

    return count


def test():
    assert one_bits(11) == 3