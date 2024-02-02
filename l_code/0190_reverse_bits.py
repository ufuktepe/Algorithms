def reverse_bits(n):
    total = 0
    for i in range(32):
        exp = 31 - i
        bit = n & 1
        total += bit * (2 ** exp)
        n = n >> 1
    return total


def test():
    assert reverse_bits(0b00000010100101000001111010011100) == 964176192