def largestRectangleArea(heights):
    maxArea = 0
    stack = []  # list[(column, height)]
    heights = [0] + heights + [0]  # append zero heights at both ends

    for i, height in enumerate(heights):
        while stack and stack[-1][1] > height:
            rect_right = i
            rect_height = stack.pop()[1]
            rect_left = stack[-1][0]
            area = (rect_right - rect_left - 1) * rect_height
            maxArea = max(area, maxArea)

        stack.append((i, height))

    return maxArea







def largest_rectangles(heights):
    heights = [0] + heights + [0]
    stack = []
    max_area = 0

    for i, height in enumerate(heights):
        while stack and heights[stack[-1]] > height:
            idx = stack.pop()
            h = heights[idx]
            w_start = stack[-1]
            w_end = i
            w = w_end - w_start - 1
            area = h * w
            max_area = max(max_area, area)
        stack.append(i)

    return max_area


def largest_rectangles_v2(heights):
    stack = []  # invariant: increasing order
    n = len(heights)
    right_smallest = [n] * n
    left_smallest = [-1] * n

    for i, height in enumerate(heights):
        while stack and heights[stack[-1]] > height:
            right_smallest[stack.pop()] = i
        stack.append(i)

    stack = []  # invariant: increasing order
    for i in range(n - 1, -1, -1):
        height = heights[i]
        while stack and heights[stack[-1]] > height:
            left_smallest[stack.pop()] = i
        stack.append(i)

    max_area = 0
    for i, (left, right) in enumerate(zip(left_smallest, right_smallest)):
        width = right - left - 1
        height = heights[i]
        area = width * height
        max_area = max(max_area, area)

    return max_area



def largest_rectangle_v3(heights):
    heights += [0]
    stack = [] # [(h, w)]
    max_area = 0

    for height in heights:
        total_w = 0
        while stack and height < stack[-1][0]:
            h, w = stack.pop()
            total_w += w
            area = total_w * h
            max_area = max(max_area, area)

        stack.append((total_w + 1, height))
    return max_area

def test():
    assert largest_rectangles_v2(heights=[5, 7, 8, 6]) == 20



