class Node:
    def __init__(self, val):
        self.val = val  # ----> YOU DON'T REALLY NEED THIS
        self.is_word = False
        self.children = {}  # Maps val to nodes


class Trie:

    def __init__(self):
        self.root = Node(val='')

    def _get_node(self, word):
        cur = self.root
        for ch in word:
            if ch not in cur.children:
                return None
            cur = cur.children[ch]
        return cur

    def insert(self, word):
        # Inserts the string word into the trie.
        cur = self.root
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = Node(ch)

            cur = cur.children[ch]
        cur.is_word = True

    def search(self, word):
        # Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
        node = self._get_node(word)
        if node is None or not node.is_word:
            return False
        return True

    def startsWith(self, prefix):
        # Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise
        node = self._get_node(prefix)
        if node is None:
            return False
        return True


def test():
    trie = Trie()
    trie.insert('weekend')
    assert trie.search('weekend')
    assert trie.startsWith('week')
    assert trie.search('week') is False
    trie.insert('week')
    assert trie.search('week')