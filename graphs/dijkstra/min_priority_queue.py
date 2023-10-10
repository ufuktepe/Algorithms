class Item:
    def __init__(self, label, key):
        self.label = label
        self.key = key


class MinPriorityQueue:
    def __init__(self):
        self.items = []
        self.pos = {}

    def is_empty(self):
        return len(self.items) == 0

    def insert(self, item):
        if item.label in self.pos:
            raise ValueError(f'Item with label {item.label} already exists.')
        self.pos[item.label] = len(self.items)
        self.items.append(item)
        self.heapify_up(item)

    def parent(self, item):
        i = self.pos[item.label]
        return self.items[(i - 1) // 2] if i > 0 else item

    def left(self, item):
        i = self.pos[item.label]
        j = i * 2 + 1
        return self.items[j] if j < len(self.items) else item

    def right(self, item):
        i = self.pos[item.label]
        j = i * 2 + 2
        return self.items[j] if j < len(self.items) else item

    def swap(self, item_1, item_2):
        i = self.pos[item_1.label]
        j = self.pos[item_2.label]

        self.items[i], self.items[j] = self.items[j], self.items[i]
        self.pos[item_1.label] = j
        self.pos[item_2.label] = i

    def heapify_up(self, item):
        parent = self.parent(item)
        if parent.key > item.key:
            self.swap(item, parent)
            self.heapify_up(item)

    def heapify_down(self, item):
        left = self.left(item)
        right = self.right(item)
        min_item = left if left.key < right.key else right

        if min_item.key < item.key:
            self.swap(item, min_item)
            self.heapify_down(item)

    def decrease_key(self, item, key):
        if item.key <= key:
            return
        item.key = key
        self.heapify_up(item)

    def extract_min(self):
        if len(self.items) == 0:
            return None
        self.swap(self.items[0], self.items[-1])
        min_item = self.items.pop()

        if len(self.items) > 0:
            self.heapify_down(self.items[0])

        return min_item


if __name__ == '__main__':
    a = Item('A', 5)
    b = Item('B', 10)
    c = Item('C', 20)
    d = Item('D', 30)
    e = Item('E', 40)
    f = Item('F', 50)

    items = [a, b, c, d, e, f]

    pq = MinPriorityQueue()
    for item in items:
        pq.insert(item)

    g = Item('G', 7)
    h = Item('H', 2)

    pq.insert(g)
    pq.insert(h)

    pq.decrease_key(f, 3)
    for i in range(len(pq.items)):
        print(f'{pq.items[i].label} {pq.items[i].key} pos: {pq.pos[pq.items[i].label]}')
