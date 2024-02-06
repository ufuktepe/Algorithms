from collections import defaultdict


def find_words(board, words):
    visited = set()
    char_map = defaultdict(list)
    for i in range(len(board)):
        for j in range(len(board[0])):
            char_map[board[i][j]].append((i, j))

    def search(r, c, word, i):
        visited.add((r, c))

        if i == len(word) - 1:
            return True

        for x, y in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
            if 0 <= x < len(board) and 0 <= y < len(board[0]) and (x, y) not in visited and board[x][y] == word[i + 1]:
                if search(x, y, word, i + 1):
                    return True

        visited.remove((r, c))
        return False

    res = []
    for word in words:
        ch = word[0]
        for i, j in char_map[ch]:
            visited = set()
            if search(i, j, word, 0):
                res.append(word)
                break
        else:
            ch = word[-1]
            for i, j in char_map[ch]:
                visited = set()
                if search(i, j, word[::-1], 0):
                    res.append(word)
                    break

    return res


def test():
    board = [["o","a","a","n"],
             ["e","t","a","e"],
             ["i","h","k","r"],
             ["i","f","l","v"]]
    words = ["oath","pea","eat","rain"]
    assert set(find_words(board, words)) == {'eat', 'oath'}