class Heap:
    def __init__(self, items):
        self.A = items
        self.size = len(items)
        self.build_max_heap()

    def insert(self, item):
        self.A.append(item)
        self.size += 1
        self.max_heapify_up(self.size - 1)

    def parent(self, i):
        p = (i - 1) // 2
        return p if i > 0 else 0

    def left(self, i):
        l = i * 2 + 1
        return l if l < self.size else i

    def right(self, i):
        r = i * 2 + 2
        return r if r < self.size else i

    def build_max_heap(self):
        for i in range(len(self.A) // 2, -1, -1):
            self.max_heapify_down(i)

    def max_heapify_up(self, i):
        # Get index of parent
        p = self.parent(i)
        if self.A[i] > self.A[p]:
            self.A[i], self.A[p] = self.A[p], self.A[i]
            self.max_heapify_up(p)

    def max_heapify_down(self, i):
        # Get the indices of children
        l = self.left(i)
        r = self.right(i)

        # index of largest child
        largest = r if self.A[l] < self.A[r] else l

        if self.A[i] < self.A[largest]:
            self.A[largest], self.A[i] = self.A[i], self.A[largest]
            self.max_heapify_down(largest)

    def delete_max(self):
        max_item = self.A[0]
        self.A[0], self.A[self.size - 1] = self.A[self.size - 1], self.A[0]
        self.size -= 1
        self.max_heapify_down(0)
        return max_item


def heap_sort(items):
    heap = Heap(items)
    for _ in range(len(items) - 1):
        # Swap first and last items
        items[heap.size - 1], items[0] = items[0], items[heap.size - 1]

        heap.size -= 1
        heap.max_heapify_down(0)


if __name__ == '__main__':
    items = [10, 40, 60, 15, 55, 80, 95, 85, 45, 50]
    heap = Heap(items)
    print(items)
    print(heap.insert(35))
    print(items)
