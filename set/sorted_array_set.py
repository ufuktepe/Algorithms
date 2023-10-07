from array_seq import ArraySeq


class SortedArraySet:
    def __init__(self):
        self.array_seq = ArraySeq()

    def __len__(self):
        return len(self.array_seq)

    def __iter__(self):
        yield from self.array_seq

    def iter_order(self):
        yield from self

    def build(self, items):
        items = self._sort(items)
        self.array_seq.build(items)

    def _sort(self, items):
        return self._merge_sort(items)

    def _merge_sort(self, items):
        if len(items) <= 1:
            return items

        mid_idx = len(items) // 2

        lst_a = self._merge_sort(items[:mid_idx])
        lst_b = self._merge_sort(items[mid_idx:])

        return self._merge(lst_a, lst_b)

    def _merge(self, lst_a, lst_b):
        counter_a = 0
        counter_b = 0
        lst_c = []

        while counter_a < len(lst_a) and counter_b < len(lst_b):
            if lst_a[counter_a].key < lst_b[counter_b].key:
                lst_c.append(lst_a[counter_a])
                counter_a += 1
            else:
                lst_c.append(lst_b[counter_b])
                counter_b += 1

        while counter_a < len(lst_a):
            lst_c.append(lst_a[counter_a])
            counter_a += 1

        while counter_b < len(lst_b):
            lst_c.append(lst_b[counter_b])
            counter_b += 1

        return lst_c

    def _binary_search(self, k, i, j):
        if i == j:
            return i

        mid_idx = (j + i) // 2
        mid_item = self.array_seq.get_at(mid_idx)

        if k == mid_item.key:
            return mid_idx
        elif k < mid_item.key:
            return self._binary_search(k, i, mid_idx - 1)
        else:
            return self._binary_search(k, mid_idx + 1, j)

    def find_min(self):
        if len(self) == 0:
            raise IndexError
        return self.array_seq.get_at(0)

    def find_max(self):
        if len(self) == 0:
            raise IndexError
        return self.array_seq.get_at(len(self) - 1)

    def find(self, k):
        if len(self) == 0:
            return None

        idx = self._binary_search(k, 0, len(self) - 1)
        item = self.array_seq.get_at(idx)
        if item.key == k:
            return item
        return None

    def find_next(self, k):
        if len(self) == 0:
            return None

        idx = self._binary_search(k, 0, len(self) - 1)
        item = self.array_seq.get_at(idx)
        if item.key > k:
            return item
        elif len(self) > idx+1:
            return self.array_seq.get_at(idx+1)
        return None

    def find_prev(self, k):
        if len(self) == 0:
            return None

        idx = self._binary_search(k, 0, len(self) - 1)
        item = self.array_seq.get_at(idx)
        if item.key < k:
            return item
        elif idx > 0:
            return self.array_seq.get_at(idx-1)
        return None

    def insert(self, item):
        if len(self) == 0:
            self.array_seq.insert_first(item)

        idx = self._binary_search(item.key, 0, len(self) - 1)
        existing_item = self.array_seq.get_at(idx)
        if existing_item.key >= item.key:
            self.array_seq.insert_at(idx, item)
        else:
            self.array_seq.insert_at(idx+1, item)

    def delete(self, k):
        if len(self) == 0:
            return None

        idx = self._binary_search(k, 0, len(self) - 1)
        item = self.array_seq.get_at(idx)

        if item.key == k:
            self.array_seq.delete_at(idx)
            return item
        return None
