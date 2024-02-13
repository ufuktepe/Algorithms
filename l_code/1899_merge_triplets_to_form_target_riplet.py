from collections import defaultdict

def remove_from_map(map, triplets, k):
    map[0][triplets[k][0]].remove(k)
    map[1][triplets[k][1]].remove(k)
    map[2][triplets[k][2]].remove(k)


def add_to_map(map, triplets, k):
    map[0][triplets[k][0]].add(k)
    map[1][triplets[k][1]].add(k)
    map[2][triplets[k][2]].add(k)


# Time: O(n^3)  Space: O(n)
def merge_triplets(triplets, target):
    map = [defaultdict(set), defaultdict(set), defaultdict(set)]

    # O(n)
    for i in range(len(triplets)):
        add_to_map(map, triplets, i)

    def search(i, j):
        if j == 2:
            return True

        for k in map[j + 1][target[j + 1]]:
            if k == i:
                if search(i, j + 1):
                    return True

            for p in range(j + 2):
                if target[p] != max(triplets[i][p], triplets[k][p]):
                    break
            else:
                for a, b in ((k, i), (i, k)):
                    orig_triplet = [x for x in triplets[a]]
                    remove_from_map(map, triplets, a)

                    triplets[a] = [max(x, y) for x, y in zip(triplets[b], triplets[a])]
                    add_to_map(map, triplets, a)

                    if search(a, j + 1):
                        return True

                    remove_from_map(map, triplets, a)
                    triplets[a] = orig_triplet
                    add_to_map(map, triplets, a)

        return False

    for i in map[0][target[0]]:
        if search(i, 0):
            return True
    return False


def test():
    triplets = [[2,5,3],[1,8,4],[1,7,5]]
    target = [2,7,5]
    assert merge_triplets(triplets, target)