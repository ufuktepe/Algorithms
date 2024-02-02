# Time: O(n*log(n))  Space: O(n)
def find_min_arrows(points):
    balloons = []
    for i, (start, end) in enumerate(points):
        balloons.append((start, 0, i))
        balloons.append((end, 1, i))

    balloons.sort()
    seen = set()
    popped = set()
    n_arrows = 0

    for x, pos, b_id in balloons:
        if pos == 0:
            seen.add(b_id)
        elif b_id not in popped:
            n_arrows += 1
            popped.update(seen)
            seen = set()

    return n_arrows


def test():
    points = [[10, 16], [2, 8], [1, 6], [7, 12]]
    assert find_min_arrows(points) == 2