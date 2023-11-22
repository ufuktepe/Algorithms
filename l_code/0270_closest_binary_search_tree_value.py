class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def closest_value(root, target):
    closest_val = root.val
    delta = abs(target - closest_val)

    cur = root
    while cur:
        cur_delta = abs(target - cur.val)
        if delta > cur_delta or (delta == cur_delta and closest_val > cur.val):
            delta = cur_delta
            closest_val = cur.val

        cur = cur.left if target <= cur.val else cur.right

    return closest_val



def test_1():
    a = Node(1)
    b = Node(2)
    c = Node(3)
    d = Node(4)
    e = Node(5)

    b.left, b.right = a, c
    d.left, d.right = b, e

    assert closest_value(d, 3.5) == 3