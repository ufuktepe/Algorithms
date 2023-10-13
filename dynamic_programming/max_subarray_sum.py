
def max_subarray_sum(a):
    n = len(a)
    max_sum = float('-inf')
    start_idx = None
    end_idx = None

    # S[i][j] is the sum of items in a[i:j+1]
    S = [[0] * n for _ in range(n)]

    # Base cases
    for i in range(n):
        S[i][i] = a[i]
        if max_sum < a[i]:
            max_sum = a[i]
            start_idx, end_idx = i, i

    for subarray_length in range(1, n + 1):
        for i in range(n - subarray_length + 1):
            j = i + subarray_length - 1
            if j == 0:
                continue
            S[i][j] = S[i][j - 1] + a[j]

            if max_sum < S[i][j]:
                max_sum = S[i][j]
                start_idx, end_idx = i, j

    return max_sum, start_idx, end_idx


def max_subarray_sum_v2(a):
    n = len(a)
    max_sum = float('-inf')
    start_idx = None
    end_idx = None

    start_indices = [i for i in range(n)]

    # x[k] is the max subarray sum ending at A[k]
    x = []
    for i in range(n):
        x.append(a[i])
        if max_sum < a[i]:
            max_sum = a[i]
            end_idx = i

    for i in range(1, n):
        if x[i] < x[i - 1] + a[i]:
            x[i] = x[i - 1] + a[i]
            start_indices[i] = start_indices[i - 1]

            if max_sum < x[i]:
                max_sum = x[i]

                end_idx = i

    return max_sum, start_indices, end_idx


if __name__ == '__main__':
    a = [-9, 1, -5, 4, 3, -6, 7, 8, -2]
    # max_sum, i, j = max_subarray_sum(a)
    # print(f'Sum: {max_sum} i:{i} j:{j}')

    max_sum, start_indices, end_idx = max_subarray_sum_v2(a)
    print(f'Sum: {max_sum} i:{start_indices[end_idx]} j:{end_idx}')