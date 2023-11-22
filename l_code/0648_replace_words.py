# Let N be the num of items in dictionary
# Let M be the num of words in sentence and W be the length of longest word
# Time: O(M*W^2)  Space: O(N + M*W)
def replace_words(dictionary, sentence):
    roots = set(dictionary)        # O(N)
    words = sentence.split()       # O(M*W)
    res = []

    # O(M*W^2)
    for word in words:
        for i in range(len(word)):
            prefix = word[:i+1]
            if prefix in roots:
                res.append(prefix)
                break
        else:
            res.append(word)

    return ' '.join(res)


class Node:
    def __init__(self):
        self.is_word = False
        self.children = {}  # Maps characters to children nodes


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = Node()
            node = node.children[ch]
        node.is_word = True

    # Time: O(N) where N is the length of the given word
    def get_shortest_prefix(self, word):
        node = self.root
        # O(N)
        for i, ch in enumerate(word):
            if ch not in node.children:
                return None
            node = node.children[ch]
            if node.is_word:
                return word[:i+1]  # O(N)

        return None


# Let N be the num of items in dictionary
# Let M be the num of words in sentence and W be the length of longest word
def replace_words_trie(dictionary, sentence):
    trie = Trie()
    # O(N)
    for word in dictionary:
        trie.insert(word)

    res = []
    words = sentence.split()  # O(M*W)

    # O(M*W)
    for word in words:
        prefix = trie.get_shortest_prefix(word)  # O(W)
        if prefix:
            res.append(prefix)
        else:
            res.append(word)

    return ' '.join(res)

def test():
    dictionary = ['ab', 'mn', 'op']
    sentence = 'the abcdf nop opqrty mndfrg'
    assert replace_words_trie(dictionary, sentence) == 'the ab nop op mn'
