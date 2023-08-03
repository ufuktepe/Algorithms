from array_seq import ArraySeq


class DynamicArraySeq(ArraySeq):
    def __init__(self, r=2):
        super().__init__()
        # self.size is the number of items in the array, not the allocated length in memory
        self.r = r
        self.upper = None
        self.lower = None

        self._compute_bounds()

    def build(self, items):
        for item in items:
            self.insert_last(item)

    def _compute_bounds(self):
        self.upper = len(self.items)
        self.lower = len(self.items) // (self.r ** 2)

    def _resize(self, n):
        if self.lower < n < self.upper:
            return
        new_items = [None] * n
        super()._copy_forward(src_idx=0, num_of_items=self.size, items=new_items, dst_idx=0)
        self.items = new_items
        self._compute_bounds()

    def insert_last(self, item):
        self._resize(self.size + 1)
        self.items[self.size] = item
        self.size += 1

    def delete_last(self):
        self.items[self.size - 1] = None
        self.size -= 1
        self._resize(self.size)

    def insert_at(self, i, item):
        self.insert_last(None)
        super()._copy_backward(src_idx=i, num_of_items=self.size-(i+1), items=self.items, dst_idx=i+1)
        self.items[i] = item

    def delete_at(self, i):
        item = self.items[i]
        super()._copy_forward(src_idx=i+1, num_of_items=self.size-(i+1), items=self.items, dst_idx=i)
        self.delete_last()
        return item

    def insert_first(self, item):
        self.insert_at(0, item)

    def delete_first(self):
        return self.delete_at(0)
