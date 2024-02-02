# Time: O(n)  Space: O(n)
def total_fruit(fruits):
    fruit_counts = {}
    max_count = 0
    left, right = 0, 0

    while right < len(fruits):
        if fruits[right] not in fruit_counts:
            fruit_counts[fruits[right]] = 0

        fruit_counts[fruits[right]] += 1

        while len(fruit_counts) > 2:
            fruit_counts[fruits[left]] -= 1
            if fruit_counts[fruits[left]] == 0:
                del fruit_counts[fruits[left]]
            left += 1

        max_count = max(max_count, right - left + 1)
        right += 1

    return max_count


def test():
    fruits = [1, 2, 3, 2, 2]
    assert total_fruit(fruits) == 4