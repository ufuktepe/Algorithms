# Time: O(n)  Space: O(n)
def plus_one(digits):
    if digits[-1] != 9:
        digits[-1] += 1
        return digits

    res = [0]
    carry = 1

    for i in range(len(digits) - 2, -1, -1):
        total = digits[i] + carry
        res.append(total % 10)
        carry = total // 10

    if carry:
        res.append(carry)

    return res[::-1]


def test():
    assert plus_one([1, 2]) == [1, 3]
    assert plus_one([9]) == [1, 0]
    assert plus_one([1, 9, 9]) == [2, 0, 0]