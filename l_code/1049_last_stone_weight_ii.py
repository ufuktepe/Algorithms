from functools import lru_cache


def last_stone_weight_ii_(stones):
    @lru_cache
    def get_min(i, v):
        if i == len(stones):
            return abs(v)

        return min(get_min(i+1, stones[i] + v), get_min(i+1, v - stones[i]))

    return get_min(0, 0)


def last_stone_weight_ii(stones):
    @lru_cache
    def get_min(i):
        if i == len(stones):
            return 0

        res1 = stones[i] + get_min(i + 1)
        res2 = -stones[i] + get_min(i + 1)

        return res1 if abs(res1) < abs(res2) else res2

    return get_min(0)

def test():
    stones = [2, 7, 4, 8, 1]
    assert last_stone_weight_ii_(stones) == 0


# def test_2():
#     stones = [2, 7, 4, 1, 8, 1]
#     assert last_stone_weight_ii(stones) == 1


# def test_3():
#     stones = [2, 7, 4, 1, 8]
#     assert last_stone_weight_ii(stones) == 0