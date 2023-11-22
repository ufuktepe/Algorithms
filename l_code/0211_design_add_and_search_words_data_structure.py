class Node:
    def __init__(self, val):
        self.val = val
        self.children = {}
        self.is_word = False


class WordDictionary:
    def __init__(self):
        self.root = Node('')

    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = Node(ch)
            node = node.children[ch]
        node.is_word = True

    def search(self, word: str) -> bool:
        stack = [(self.root, 0)]

        while stack:
            node, i = stack.pop()
            ch = word[i]

            if ch == '.':
                if i == len(word) - 1:
                    for child in node.children.values():
                        if child.is_word:
                            return True
                else:
                    for child in node.children.values():
                        stack.append((child, i + 1))
            else:
                if ch not in node.children:
                    continue
                if i == len(word) - 1:
                    if node.children[ch].is_word:
                        return True
                else:
                    stack.append((node.children[ch], i + 1))

        return False


def test():
    wd = WordDictionary()
    words = ['agz', 'apple', 'orange']
    for word in words:
        wd.addWord(word)

    assert wd.search('orange')
    assert wd.search('ora') is False
    assert wd.search('ap.le')
    assert wd.search('orang.')
    assert wd.search('orange.') is False
    assert wd.search('..z')