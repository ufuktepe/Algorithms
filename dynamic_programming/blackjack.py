# MIT 6.006 Recitation 15 (2020)
def blackjack(deck):
    n = len(deck)
    num_of_wins = [0 for _ in range(n + 1)]  # maps num of drawn cards to num of wins

    for i in range(n):  # i is the number of cards drawn so far
        if n - i < 5:
            break
        dealer = deck[i] + deck[i + 1]
        player = deck[i + 2] + deck[i + 3]

        if dealer < player <= 21:
            num_of_wins[i + 4] = max(num_of_wins[i + 4], num_of_wins[i] + 1)

        player += deck[i + 4]

        if dealer < player <= 21:
            num_of_wins[i + 5] = max(num_of_wins[i + 5], num_of_wins[i] + 1)

    return num_of_wins


if __name__ == '__main__':
    deck = [5, 4, 7, 2, 1, 9, 9, 2, 7, 10]
    num_of_wins = blackjack(deck)

    for i in num_of_wins:
        print(i)