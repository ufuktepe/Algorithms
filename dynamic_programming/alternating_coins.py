
def alt_coins(coins):
    n = len(coins)

    my_moves = [[None for p in range(n)] for q in range(n)]
    your_moves = [[None for p in range(n)] for q in range(n)]

    # M[i][j] is the max points I can get if it's my turn and the remaining coins start at index i and end at j
    M = [[0] * n for _ in range(n)]

    # Base Cases: if only one coin is left, and it's my turn, then I get the coin
    for i in range(n):
        M[i][i] = coins[i]

    # Y[i][j] is the max points I can get if it's opponent's turn and the remaining coins start at index i and end at j
    Y = [[0] * n for _ in range(n)]

    # n_coins is the remaining number of coins
    for n_coins in range(1, n + 1):
        for i in range(n - n_coins + 1):
            j = i + n_coins - 1

            if i == n - 1 or j == 0:
                continue

            if Y[i + 1][j] + coins[i] > Y[i][j - 1] + coins[j]:
                M[i][j] = Y[i + 1][j] + coins[i]
                my_moves[i][j] = i
            else:
                M[i][j] = Y[i][j - 1] + coins[j]
                my_moves[i][j] = j

            if M[i + 1][j] < M[i][j - 1]:
                Y[i][j] = M[i + 1][j]
                your_moves[i][j] = i
            else:
                Y[i][j] = M[i][j - 1]
                your_moves[i][j] = j

    return M, Y, my_moves, your_moves


def print_square_matrix(A):
    n = len(A)
    for i in range(n):
        for j in range(n):
            print(A[i][j], end=' ')
        print('')


if __name__ == '__main__':
    coins = [5, 10, 100, 25]
    M, Y, my_moves, your_moves = alt_coins(coins)

    print('Max Scores-----------------------')
    print_square_matrix(M)
    print('My moves-----------------------')
    print_square_matrix(my_moves)
    print('Your Moves-----------------------')
    print_square_matrix(your_moves)
