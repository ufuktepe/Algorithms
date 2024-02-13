from collections import deque, defaultdict

# Time: O(n)  Space: O(n)
def distance_k(root, target, k):
    adj = defaultdict(list)  # maps node values to adjacent nodes
    q = deque([root])

    while q:
        node = q.popleft()

        if node.left is not None:
            adj[node.left.val].append(node)
            adj[node.val].append(node.left)
            q.append(node.left)
        if node.right is not None:
            adj[node.right.val].append(node)
            adj[node.val].append(node.right)
            q.append(node.right)

    q = deque([target])
    res = []
    dist = 0
    visited = {target.val}

    while q:
        n = len(q)

        for _ in range(n):
            node = q.popleft()

            if dist == k:
                res.append(node.val)
            else:
                for adj_node in adj[node.val]:
                    if adj_node.val not in visited:
                        visited.add(adj_node.val)
                        q.append(adj_node)

        dist += 1

    return res


