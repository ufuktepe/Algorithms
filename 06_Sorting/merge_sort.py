def merge_sort(lst):
    if len(lst) == 0:
        return []
    if len(lst) == 1:
        return lst

    mid_index = len(lst) // 2

    lst_a = merge_sort(lst[:mid_index])
    lst_b = merge_sort(lst[mid_index:])

    return merge(lst_a, lst_b)


def merge(lst_a, lst_b):
    output_lst = []
    counter_a = 0
    counter_b = 0

    while counter_a < len(lst_a) and counter_b < len(lst_b):

        if lst_a[counter_a] < lst_b[counter_b]:
            output_lst.append(lst_a[counter_a])
            counter_a += 1
        else:
            output_lst.append(lst_b[counter_b])
            counter_b += 1

    while counter_a < len(lst_a):
        output_lst.append(lst_a[counter_a])
        counter_a += 1

    while counter_b < len(lst_b):
        output_lst.append(lst_b[counter_b])
        counter_b += 1

    return output_lst


a = [3, 6, 10, 2, 1, 4, 9, 5, 8, 7]

print(merge_sort(a))
