from collections import defaultdict


# Time: O(N + M)  Space: O(N + M)
def find_order(prerequisites, numCourses):
    adj = defaultdict(list)

    # O(M)
    for post, prev in prerequisites:
        adj[prev].append(post)

    post_order = []
    # O(N)
    visited = [0] * numCourses  # 0=not visited, 1=visiting, 2=visited

    def dfs(course):
        visited[course] = 1

        for next_course in adj[course]:
            if visited[next_course] == 2:
                continue
            if visited[next_course] == 1:
                return False

            if not dfs(next_course):
                return False


        post_order.append(course)
        visited[course] = 2
        return True

    # O(N + M)
    for course in range(numCourses):
        if not visited[course]:
            if not dfs(course):
                return []

    return post_order[::-1]


def test():
    prerequisites = [[6, 4], [5, 1], [2, 1], [6, 3], [2, 5], [1, 0], [4, 5], [4, 2], [3, 4], [3, 2]]
    assert find_order(prerequisites, 7) == [0, 1, 5, 2, 4, 3, 6]