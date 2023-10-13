
def lis(a):
    # S[i] represents the length of the longest increasing subsequence ending with a[i]
    S = [1 for _ in range(len(a))]

    # P stores parent pointers to reconstruct the lis
    P = [None for _ in range(len(a))]

    for i in range(1, len(a)):
        for j in range(i):
            if a[i] > a[j] and S[i] < S[j] + 1:
                S[i] = S[j] + 1
                P[i] = j
    return S, P


def print_lis(P, a, i):
    parent_index = P[i]
    if parent_index is not None:
        print_lis(P, a, parent_index)
    print(a[i], end='')


if __name__ == '__main__':
    a = 'carbohydrate'
    S, P = lis(a)

    max_lis_len = 0
    idx = None
    for i, lis_len in enumerate(S):
        if max_lis_len < lis_len:
            max_lis_len = lis_len
            idx = i

    print_lis(P, a, idx)
