

def bowling(pin_values):
    n = len(pin_values) - 1
    max_scores = [0 for _ in range(n + 1)]

    for i in range(1, n + 1):
        # Case 1: don't hit the pin
        s1 = max_scores[i - 1]

        # Case 2: hit the pin
        s2 = max_scores[i - 1] + pin_values[i]

        # Case 3: hit the pin and the previous one
        s3 = 0 if i < 2 else max_scores[i - 2] + pin_values[i] * pin_values[i - 1]

        max_scores[i] = max(s1, s2, s3)

    return max_scores[-1]


if __name__ == '__main__':
    pin_values = [None, -1, 1, 1, 1, 9, 9, 3, -3, -5, 2, 2]
    print(bowling(pin_values))
