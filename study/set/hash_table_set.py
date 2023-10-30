from random import randint

from study.linked_lists.singly_linked_list import SinglyLinkedList
from study.set.set_from_seq import SetFromSeq


class HashTableSet:
    def __init__(self, r=200):
        self.A = []
        self.size = 0
        self.r = r      # 100/self.r = fill ratio
        self.p = 2**31 - 1
        self.a = randint(1, self.p - 1)
        self.lower = None
        self.upper = None
        self._compute_bounds()
        self._resize(0)

    def __len__(self):
        return self.size

    def __iter__(self):
        for X in self.A:
            yield from X

    def _compute_bounds(self):
        self.upper = len(self.A)
        self.lower = len(self.A) * 100*100 // (self.r*self.r)

    def _hash(self, k, m):
        return ((self.a * k) % self.p) % m

    def _resize(self, n):
        if self.lower < n < self.upper:
            return

        f = self.r // 100
        if self.r % 100: f += 1
        # f = ceil(r / 100)
        m = max(n, 1) * f
        A = [SetFromSeq(SinglyLinkedList) for _ in range(m)]
        for x in self:
            h = self._hash(x.key, m)
            A[h].insert(x)
        self.A = A
        self._compute_bounds()

    def build(self, X):
        for item in X:
            self.insert(item)

    def insert(self, item):
        self._resize(self.size + 1)
        hash_val = self._hash(k=item.key, m=len(self.A))
        self.A[hash_val].insert(item)
        self.size += 1

    def find(self, k):
        hash_val = self._hash(k=k, m=len(self.A))
        return self.A[hash_val].find(k)

    def delete(self, k):
        hash_val = self._hash(k=k, m=len(self.A))
        item = self.A[hash_val].delete(k)
        self.size -= 1
        self._resize(self.size)
        return item

    def find_min(self):
        min_item = None
        for item in self:
            if min_item is None or min_item.key > item.key:
                min_item = item
        return min_item

    def find_max(self):
        max_item = None
        for item in self:
            if max_item is None or max_item.key < item.key:
                max_item = item
        return max_item

    def find_next(self, k):
        next_item = None
        for item in self:
            if item.key > k:
                if next_item is None or next_item.key > item.key:
                    next_item = item
        return next_item

    def find_prev(self, k):
        prev_item = None
        for item in self:
            if item.key < k:
                if prev_item is None or prev_item.key < item.key:
                    prev_item = item
        return prev_item

    def iter_order(self):
        item = self.find_min()
        while item:
            yield item
            item = self.find_next(item.key)


