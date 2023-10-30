

def lcs(a, b):
    # S[n][m] contains the lcs length using the first n letters from a and m letters from b
    S = [[0 for j in range(len(b) + 1)] for i in range(len(a) + 1)]

    # P stores parent pointers to reconstruct the LCS
    P = [[None for j in range(len(b) + 1)] for i in range(len(a) + 1)]

    for i in range(len(a)):
        n = i + 1
        for j in range(len(b)):
            m = j + 1
            if a[i] == b[j]:
                S[n][m] = 1 + S[n - 1][m - 1]
                P[n][m] = (n - 1, m - 1)
            elif S[n - 1][m] > S[n][m - 1]:
                S[n][m] = S[n - 1][m]
                P[n][m] = (n - 1, m)
            else:
                S[n][m] = S[n][m - 1]
                P[n][m] = (n, m - 1)

    return S, P


def print_lcs(P, a, b, n, m):
    if n == 0 or m == 0:
        return
    new_n, new_m = P[n][m]
    print_lcs(P, a, b, new_n, new_m)
    if n > new_n and m > new_m:
        print(a[n - 1], end='')  # Same as b[m - 1]


if __name__ == '__main__':
    a = 'ACCGGTCGAGTGCGCGGAAGCCGGCCGAA'
    b = 'GTCGTTCGGAATGCCGTTGCTCTGTAAA'
    S, P = lcs(a, b)

    n = len(a)
    m = len(b)
    print_lcs(P, a, b, n, m)