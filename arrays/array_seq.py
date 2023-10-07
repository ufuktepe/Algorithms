class ArraySeq:
    def __init__(self):
        self.items = []
        self.size = 0

    def __len__(self):
        return self.size

    def __iter__(self):
        yield from self.items

    def build(self, items):
        self.items = [item for item in items]
        self.size = len(self.items)

    def get_at(self, i):
        return self.items[i]

    def set_at(self, i, item):
        self.items[i] = item

    def _copy_forward(self, src_idx, num_of_items, items, dst_idx):
        for i in range(num_of_items):
            items[dst_idx + i] = self.items[src_idx + i]

    def _copy_backward(self, src_idx, num_of_items, items, dst_idx):
        for i in range(num_of_items - 1, -1, -1):
            items[dst_idx + i] = self.items[src_idx + i]

    def insert_at(self, i, item):
        if not (0 <= i <= self.size):
            raise IndexError
        new_items = [None] * (self.size + 1)
        self._copy_forward(src_idx=0, num_of_items=i, items=new_items, dst_idx=0)
        new_items[i] = item
        self._copy_forward(src_idx=i, num_of_items=self.size-i, items=new_items, dst_idx=i+1)
        self.build(new_items)

    def delete_at(self, i):
        if not (0 <= i < self.size):
            raise IndexError
        item = self.items[i]
        new_items = [None] * (self.size - 1)
        self._copy_forward(src_idx=0, num_of_items=i, items=new_items, dst_idx=0)
        self._copy_forward(src_idx=i+1, num_of_items=self.size-i-1, items=new_items, dst_idx=i)
        self.build(new_items)

        return item

    def insert_first(self, item):
        self.insert_at(0, item)

    def delete_first(self):
        self.delete_at(0)

    def insert_last(self, item):
        self.insert_at(self.size, item)

    def delete_last(self):
        self.delete_at(self.size - 1)