from collections import defaultdict


# Time: O(N+M)  Space: O(N+M)
def min_num_of_semesters(n, relations):
    adj = defaultdict(list)
    in_degree = {course: 0 for course in range(1, n + 1)}

    for prev, nxt in relations:
        adj[prev].append(nxt)
        in_degree[nxt] += 1

    q = []

    for course, degree in in_degree.items():
        if degree == 0:
            q.append(course)

    n_semesters = 0
    processed = 0
    while q:
        n_semesters += 1
        next_q = []
        processed += len(q)
        for course in q:
            for next_course in adj[course]:
                in_degree[next_course] -= 1
                if in_degree[next_course] == 0:
                    next_q.append(next_course)
        q = next_q

    if processed != n:
        return -1

    return n_semesters


def test():
    relations = [[1,3],[2,3]]
    n = 3
    assert min_num_of_semesters(n, relations) == 2