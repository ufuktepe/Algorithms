from collections import defaultdict

NOT_VISITED = 0
VISITING = 1
VISITED = 2


def alien_order(words):
    adj = {}

    for word in words:
        for ch in word:
            adj[ch] = set()

    for first_word, second_word in zip(words, words[1:]):
        for first_ch, second_ch in zip(first_word, second_word):
            if first_ch == second_ch:
                continue
            adj[first_ch].add(second_ch)
            break
        else:
            if len(second_word) < len(first_word):
                return ''

    post_order = []
    visited = {ch: NOT_VISITED for ch in adj}

    def dfs(letter):
        visited[letter] = VISITING

        for next_letter in adj[letter]:
            if visited[next_letter] == VISITING:
                return False
            if visited[next_letter] == NOT_VISITED:
                if not dfs(next_letter):
                    return False

        visited[letter] = VISITED
        post_order.append(letter)
        return True

    for letter in adj:
        if visited[letter] == NOT_VISITED:
            if not dfs(letter):
                return ''

    return ''.join(post_order[::-1])


def test():
    words = ['abc', 'ab']
    assert alien_order(words) == ""


def test_2():
    words = ["wrt", "wrf", "er", "ett", "rftt"]
    assert alien_order(words) == "wertf"