class Node:
    def __init__(self, key=None, val=None, next=None):
        self.key = key
        self.val = val
        self.next = next


class MyHashMap:
    SIZE = 10 ** 4

    def __init__(self):
        self.arr = [Node()] * self.SIZE

    def _hash(self, key):
        return key % self.SIZE

    def _get_node(self, key):
        index = self._hash(key)
        cur = self.arr[index]

        while cur:
            if cur.key == key:
                return cur
            cur = cur.next

        return None

    def _add_node(self, node):
        index = self._hash(node.key)
        cur = self.arr[index]

        while cur.next:
            cur = cur.next

        cur.next = node

    def put(self, key: int, value: int) -> None:
        """inserts a (key, value) pair into the HashMap. If the key already exists in the map, update the corresponding value."""

        # check if already exists
        node = self._get_node(key)
        if node is None:
            node = Node(key, value)
            self._add_node(node)
        else:
            node.val = value

    def get(self, key: int) -> int:
        """returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key."""
        node = self._get_node(key)
        if node is None:
            return -1
        return node.val

    def remove(self, key: int) -> None:
        """removes the key and its corresponding value if the map contains the mapping for the key."""
        index = self._hash(key)
        prev = self.arr[index]
        cur = prev.next

        while cur:
            if cur.key == key:
                prev.next = cur.next
            prev = cur
            cur = cur.next


def test():
    my_hash_map = MyHashMap()
    keys = [1, 2, 3, 4, 4, 5]
    vals = [10, 20, 30, 40, 45, 50]

    for k, v in zip(keys, vals):
        my_hash_map.put(k, v)

    assert my_hash_map.get(1) == 10
    assert my_hash_map.get(4) == 45
    assert my_hash_map.get(7) == -1
    my_hash_map.remove(4)
    assert my_hash_map.get(4) == -1