
def edit_distance(a, b):
    n, m = len(a), len(b)

    # s[i][j] is the edit distance using i characters of a and j characters of b
    s = [[None for j in range(m + 1)] for i in range(n + 1)]
    edits = [[None for j in range(m + 1)] for i in range(n + 1)]

    # Base cases
    for j in range(m + 1):
        s[0][j] = j
        edits[0][j] = '+'
    for i in range(n + 1):
        s[i][0] = i
        edits[i][0] = '+'

    edits[0][0] = None

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i - 1] == b[j - 1]:
                s[i][j] = s[i - 1][j - 1]
            else:
                s1 = s[i][j - 1] + 1      # Cost to add b[j - 1] to a
                s2 = s[i - 1][j] + 1      # Cost to remove a[i - 1] from a
                s3 = s[i - 1][j - 1] + 1  # Cost to replace a[i - 1] with b[j - 1]
                s_min = min(s1, s2, s3)
                if s_min == s1:
                    edits[i][j] = '+'
                elif s_min == s2:
                    edits[i][j] = '-'
                else:
                    edits[i][j] = 'r'
                s[i][j] = s_min

    return s, edits


def print_matrix(a, n, m):
    for i in range(n):
        for j in range(m):
            print(a[i][j], end=' ')
        print('')


def print_edits(edits, a, b, n, m):
    if n < 0 or m < 0:
        return
    if edits[n][m] == '+':
        print_edits(edits, a, b, n, m - 1)
        print(f'add {b[m - 1]} to a')
    elif edits[n][m] == '-':
        print_edits(edits, a, b, n - 1, m)
        print(f'remove {a[n - 1]} from a')
    elif edits[n][m] == 'r':
        print_edits(edits, a, b, n - 1, m - 1)
        print(f'replace {a[n - 1]} with {b[m - 1]}')
    else:
        print_edits(edits, a, b, n - 1, m - 1)


if __name__ == '__main__':
    a = 'kefvaksai'
    b = 'kavasaki'
    n, m = len(a), len(b)

    s, edits = edit_distance(a, b)

    print_edits(edits, a, b, n, m)