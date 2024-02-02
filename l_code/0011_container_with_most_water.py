def max_area(height):
    i, j = 0, len(height) - 1
    max_area = 0

    while i < j:
        max_area = max(max_area, min(height[i], height[j]) * (j - i))

        if height[i] < height[j]:
            i += 1
        else:
            j -= 1

    return max_area


def test():
    height = [10, 20, 90, 100, 40, 90]
    assert max_area(height) == 90