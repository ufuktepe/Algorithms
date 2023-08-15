def insertion_sort(lst, n):
    # Sort first n items.
    if n <= 1:
        return

    insertion_sort(lst, n - 1)
    insert_last(lst, n)


def insert_last(lst, n):
    # Assume first n-1 items are sorted, sort first n items.
    if n <= 1:
        return

    if lst[n - 2] > lst[n - 1]:
        lst[n - 2], lst[n - 1] = lst[n - 1], lst[n - 2]
        insert_last(lst, n - 1)


a = [3, 6, 10, 2, 1, 4, 9, 5, 8, 7]

insertion_sort(a, len(a))

print(a)