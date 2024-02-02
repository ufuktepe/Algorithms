def trap(height):
    n = len(height)
    bound = [0] * n

    left_max = 0
    for i in range(n):
        bound[i] = left_max
        left_max = max(left_max, height[i])

    right_max = 0
    for i in range(n - 1, -1, -1):
        bound[i] = min(bound[i], right_max)
        right_max = max(right_max, height[i])

    total = 0
    for i in range(n):
        total += max(0, bound[i] - height[i])

    return total


def trap_v2(height):
    n = len(height)
    stack = []  # invariant: non-increasing order

    total_volume = 0
    for i in range(n):
        cur_h = height[i]
        total_w = 0
        volume = 0
        while len(stack) > 1 and stack[-1][0] < cur_h:
            h, w = stack.pop()
            total_w += w
            delta_h = min(cur_h, stack[-1][0]) - h
            if delta_h >= 0:
                volume += total_w * delta_h
            else:
                total_w = 0

        total_volume += volume
        stack.append((cur_h, total_w + 1))

    return total_volume


def test():
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    assert trap_v2(height) == 6