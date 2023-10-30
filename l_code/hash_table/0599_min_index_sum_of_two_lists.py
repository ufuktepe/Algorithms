def find_restaurant(list1, list2):
    """
    :type list1: List[str]
    :type list2: List[str]
    :rtype: List[str]
    """
    map2 = {string: i for i, string in enumerate(list2)}

    output = []
    idx_sum = float('inf')

    for i, string in enumerate(list1):
        if string in map2:
            curr_idx_sum = i + map2[string]
            if idx_sum > curr_idx_sum:
                idx_sum = curr_idx_sum
                output = [string]
            elif idx_sum == curr_idx_sum:
                output.append(string)

    return output


def test_1_common_string():
    list1 = ['a', 'b', 'c', 'd']
    list2 = ['c', 'f']
    assert find_restaurant(list1, list2) == ['c']


def test_2_common_strings():
    list1 = ['a', 'b', 'c', 'd']
    list2 = ['d', 'f', 'h', 'a']
    assert find_restaurant(list1, list2) == ['a', 'd']