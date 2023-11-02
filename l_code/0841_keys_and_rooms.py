def can_visit_all_rooms(rooms):
    """
    :type rooms: List[List[int]]
    :rtype: bool
    """
    stack = [0]
    visited = {0}

    while stack:
        room = stack.pop()
        keys = rooms[room]

        for k in keys:
            if k not in visited:
                stack.append(k)
                visited.add(k)

    return len(visited) == len(rooms)


def test_success():
    rooms = [[1, 3], [3], [], [2]]
    assert can_visit_all_rooms(rooms) == True


def test_failure():
    rooms = [[2, 3], [3], [4], [3], [0]]
    assert can_visit_all_rooms(rooms) == False
