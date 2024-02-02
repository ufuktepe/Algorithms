import heapq
from collections import Counter


def least_interval(tasks, n):
    if n == 0:
        return len(tasks)

    # O(n)
    task_counts = Counter(tasks)
    heap = []
    history = {}

    # O(n)
    for task, count in task_counts.items():
        heap.append([-count, task])
        history[task] = None

    heapq.heapify(heap)

    t = 0
    done = 0

    while done < len(tasks):
        t += 1
        temp = []
        while heap:
            c, task = heapq.heappop(heap)

            if history[task] is None or t - history[task] > n:
                done += 1
                c += 1
                history[task] = t
                if c != 0:
                    heapq.heappush(heap, [c, task])
                break
            else:
                temp.append((c, task))

        for c, task in temp:
            heapq.heappush(heap, [c, task])

    return t


def test():
    tasks = ["A", "A", "A", "B", "B", "B"]
    n = 2
    assert least_interval(tasks, n) == 8