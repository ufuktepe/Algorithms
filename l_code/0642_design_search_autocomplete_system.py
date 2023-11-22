from typing import List


class Node:
    def __init__(self, sentence):
        self.sentence = sentence
        self.score = 0
        self.children = {}


class Trie:
    def __init__(self):
        self.root = Node('')

    # O(N)
    def insert(self, sentence, score):
        node = self.root
        for i, ch in enumerate(sentence):
            if ch not in node.children:
                node.children[ch] = Node(sentence[:i + 1])
            node = node.children[ch]
        node.score = score

    # O(N)
    def increment_score(self, sentence):
        node = self.root
        for i, ch in enumerate(sentence):
            if ch not in node.children:
                node.children[ch] = Node(sentence[:i + 1])
            node = node.children[ch]

        node.score += 1

    def get_top_sentences(self, prefix, k=3):
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return []
            node = node.children[ch]

        sentences = []
        stack = [node]

        while stack:
            node = stack.pop()
            if node.score:
                sentences.append((-node.score, node.sentence))

            for child in node.children.values():
                stack.append(child)

        sentences.sort()

        res = []
        for _, sentence in sentences:
            res.append(sentence)
            if len(res) == k:
                break

        return res


class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.trie = Trie()
        for sentence, score in zip(sentences, times):
            self.trie.insert(sentence, score)
        self.curr_sentence = ''

    def input(self, c):
        if c == '#':
            self.trie.increment_score(self.curr_sentence)
            self.curr_sentence = ''
            return []

        self.curr_sentence += c
        return self.trie.get_top_sentences(self.curr_sentence)



def test():
    sentences = ["i love you", "island", "iroman", "i love leetcode"]
    times = [5, 3, 2, 2]
    acs = AutocompleteSystem(sentences, times)
    assert acs.input('i') == ["i love you", "island", "i love leetcode"]