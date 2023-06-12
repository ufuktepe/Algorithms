from queue_array_based import Queue


def test_enqueue():
    queue = Queue()
    queue.enqueue(5)
    queue.enqueue(6)

    assert queue.first() == 5


def test_dequeue():
    queue = Queue()
    queue.enqueue(5)
    item = queue.dequeue()

    assert item == 5
    assert queue.is_empty()


def test_dequeue_empty_queue():
    queue = Queue()
    queue.enqueue(5)
    queue.dequeue()
    item = queue.dequeue()

    assert item is None
    assert queue.is_empty()


def test_is_empty():
    queue = Queue()

    assert queue.is_empty()