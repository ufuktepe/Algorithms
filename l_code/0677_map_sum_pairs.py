class Node:
    def __init__(self, val=0):
        self.val = val
        self.children = {}  # Maps characters to Nodes


class MapSum:

    def __init__(self):
        self.root = Node()

    # Time: O(N) Space: O(N) where N is the length of the given key
    def insert(self, key: str, val: int) -> None:
        node = self.root
        for ch in key:
            if ch not in node.children:
                node.children[ch] = Node()
            node = node.children[ch]
        node.val = val

    # Time: O(N) Space: O(N) where N is the number of nodes in the tree rooted at prefix
    def sum(self, prefix: str) -> int:
        total = 0
        node = self.root

        for ch in prefix:
            if ch not in node.children:
                return total
            node = node.children[ch]

        stack = [node]

        while stack:
            cur = stack.pop()
            total += cur.val

            for child in cur.children.values():
                stack.append(child)

        return total

def test():
    map_sum = MapSum()
    map_sum.insert('app', 3)
    map_sum.insert('applet', 2)
    map_sum.insert('applause', 4)
    map_sum.insert('application', 3)

    assert map_sum.sum('app') == 12