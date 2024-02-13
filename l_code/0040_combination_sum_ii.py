def comb_sum(candidates, target):
    candidates.sort()

    res = []

    def find(i, nums, target):
        for j in range(i, len(candidates)):
            if target - candidates[j] < 0:
                break

            if j > i and candidates[j] == candidates[j - 1]:
                continue
            new_nums = nums[:]
            new_nums.append(candidates[j])
            if target - candidates[j] == 0:
                res.append(new_nums)
                break
            else:
                find(j + 1, new_nums, target - candidates[j])

    find(0, [], target)

    return res


def test():
    candidates =[2, 5, 2, 1, 2]
    target = 5
    assert comb_sum(candidates, target) == [[1, 2, 2], [5]]