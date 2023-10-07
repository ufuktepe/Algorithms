class SetFromSeq:
    def __init__(self, seq):
        self.sequence = seq()

    def build(self, items):
        self.sequence.build(items)

    def insert(self, item):
        for i in range(len(self.sequence)):
            existing_item = self.sequence.get_at(i)
            if existing_item.key == item.key:
                self.sequence.set_at(i, item)
                return
        self.sequence.insert_last(item)

    def delete(self, item):
        for i in range(len(self.sequence)):
            existing_item = self.sequence.get_at(i)
            if existing_item.key == item.key:
                return self.sequence.delete_at(i)
        return None

    def find(self, k):
        for i in range(len(self.sequence)):
            existing_item = self.sequence.get_at(i)
            if existing_item.key == k:
                return existing_item
        return None

    def find_min(self):
        min_item = None
        for i in range(len(self.sequence)):
            item = self.sequence.get_at(i)
            if min_item is None or min_item.key > item.key:
                min_item = item
        return min_item

    def find_max(self):
        max_item = None
        for i in range(len(self.sequence)):
            item = self.sequence.get_at(i)
            if max_item is None or max_item.key < item.key:
                max_item = item
        return max_item

    def find_next(self, k):
        next_item = None
        for i in range(len(self.sequence)):
            item = self.sequence.get_at(i)
            if item.key > k:
                if next_item is None or next_item.key > item.key:
                    next_item = item
        return next_item

    def find_prev(self, k):
        prev_item = None
        for i in range(len(self.sequence)):
            item = self.sequence.get_at(i)
            if item.key < k:
                if prev_item is None or prev_item.key < item.key:
                    prev_item = item
        return prev_item
