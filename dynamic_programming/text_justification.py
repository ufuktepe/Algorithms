def text_justification(word_widths, line_width):
    n = len(word_widths)
    S = [float('inf') for _ in range(n + 1)]  # S[n] is the sum of badness over all lines using the first n words
    S[0] = 0

    for i in range(1, n + 1):
        k = 1  # number of words in the last line
        w = word_widths[i - k]  # sum of word widths in the last line
        while w <= line_width:
            line_badness = (line_width - w) ** 3
            S[i] = min(S[i], S[i - k] + line_badness)

            k += 1
            if i < k:
                break
            w += word_widths[i - k]

    return S


if __name__ == '__main__':
    word_widths = [3, 4, 2, 6, 1]
    S = text_justification(word_widths, 10)
    print(S)