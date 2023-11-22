# Time: O(log(N))  Space: O(1)
def next_greatest_letter(letters, target):
    left, right = 0, len(letters) - 1

    while left < right:
        mid = (left + right) // 2
        if letters[mid] <= target:
            left = mid + 1
        else:
            right = mid

    return letters[left] if letters[left] > target else letters[0]


def test_1():
    letters = 'bbbccccdddd'
    target = 'a'
    assert next_greatest_letter(letters, target) == 'b'
    target = 'b'
    assert next_greatest_letter(letters, target) == 'c'
    target = 'c'
    assert next_greatest_letter(letters, target) == 'd'
    target = 'd'
    assert next_greatest_letter(letters, target) == 'b'