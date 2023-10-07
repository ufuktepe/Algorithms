def selection_sort(lst, n):
    if n == 0:
        return

    i = get_index_of_max_item(lst, n)      # O(n)
    lst[n-1], lst[i] = lst[i], lst[n-1]

    selection_sort(lst, n-1)               # O(n^2)


def get_index_of_max_item(lst, n):
    if n == 1:
        return 0

    j = get_index_of_max_item(lst, n - 1)
    if lst[j] > lst[n - 1]:
        return j
    return n - 1


a = []

selection_sort(a, len(a))

print(a)
