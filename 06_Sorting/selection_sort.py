def selection_sort(lst, n):
    if n == 1:
        return

    max_idx = get_index_of_max_item(lst, n)
    lst[n-1], lst[max_idx] = lst[max_idx], lst[n-1]

    selection_sort(lst, n-1)                            # O(n)


def get_index_of_max_item(lst, n):
    if n == 1:
        return 0

    j = get_index_of_max_item(lst, n - 1)
    if lst[j] > lst[n - 1]:
        return j
    return n - 1


a = [3, 6, 10, 2, 1, 4, 9, 5, 8, 7]

selection_sort(a, len(a))

print(a)
