def print_bits(x):
    bits = []
    while x:
        bits.append(x & 1)
        x = x >> 1

    for bit in bits[::-1]:
        print(bit, end='')


print_bits(29)