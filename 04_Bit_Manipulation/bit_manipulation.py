def is_bit_set(num, position):
    mask = 1 << position
    return num & mask

def modify_bit(num, position, state):
    mask = 1 << position
    if state:
        return num | mask
    return num & ~mask

def is_even(num):
    return not (num & 1)

def is_power_of_two(num):
    return not (num & num-1)

def num_of_different_bits(num1, num2):
    delta = num1 ^ num2
    count = 0
    for i in range(32):
        count += delta >> i & 1
    return count


def count_set_bits(num):
    count = 0
    while (num):
        num = num & (num - 1)
        count += 1
    return count

def get_min(x, y):
    # if x < y then -(x < y) is -1 which is all 1's in twos complement representation. Hence, we have y ^ (x ^ y) = x
    # if x >= y then -(x < y) is 0. Hence we have y ^ 0 = y
    return y ^ ((x ^ y) & -(x < y))


# Least significant 1 = x & -x

num1 = 15
num2 = -15

print(f'Min is {get_min(num1, num2)}')
