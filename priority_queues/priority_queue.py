class PriorityQueue:
    """Takes an entire array A of elements, and maintains the queue
    itself in the prefix of the first n elements of A (where n <= len(A))"""
    def __init__(self, items):
        self.n = 0
        self.A = items

    def insert(self):
        """Absorb A[n] into the queue."""
        if self.n >= len(self.A):
            raise IndexError('Priority queue is full.')
        self.n += 1

    def delete_max(self):
        """Remove A[n - 1] from the queue."""
        if self.n == 0:
            raise IndexError('Priority queue is empty.')
        self.n -= 1  # NOT correct on its own!

    @classmethod
    def sort(Queue, A):
        pq = Queue(A)
        for _ in range(len(A)):
            pq.insert()
        for _ in range(len(A)):
            pq.delete_max()
        return pq.A

