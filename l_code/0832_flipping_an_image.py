# Time: O(n)  Space: O(1)
def flip_and_invert(image):
    n = len(image)

    for row in image:
        left, right = 0, n - 1
        while left <= right:
            row[left], row[right] = row[right] ^ 1, row[left] ^ 1
            left += 1
            right -= 1

    return image


def test():
    image = [[1, 0, 1],
             [0, 0, 1],
             [1, 1, 1]]
    assert flip_and_invert(image) == [[0, 1, 0],
                                      [0, 1, 1],
                                      [0, 0, 0]]