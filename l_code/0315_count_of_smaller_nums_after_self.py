def count_smaller(nums):
    counts = [0] * len(nums)
    aug_nums = [(i, num) for i, num in enumerate(nums)]

    def merge_sort(vals):
        if len(vals) < 2:
            return vals
        mid = len(vals) // 2
        left_sorted = merge_sort(vals[:mid])
        right_sorted = merge_sort(vals[mid:])
        return merge(left_sorted, right_sorted)

    def merge(left_lst, right_lst):
        i, j = 0, 0
        merged = []
        count = 0
        while i < len(left_lst) and j < len(right_lst):
            if left_lst[i][1] > right_lst[j][1]:
                merged.append(right_lst[j])
                count += 1
                j += 1
            else:
                merged.append(left_lst[i])
                counts[left_lst[i][0]] += count
                i += 1


        while i < len(left_lst):
            merged.append(left_lst[i])
            counts[left_lst[i][0]] += count
            i += 1


        while j < len(right_lst):
            merged.append(right_lst[j])
            j += 1

        return merged

    merge_sort(aug_nums)

    return counts


def test():
    nums = [5, 2, 6, 1]
    assert count_smaller(nums) == [2, 1, 1, 0]