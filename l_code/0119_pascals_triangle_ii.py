
def get_row(row_idx):
    def generate_next_row(row):
        next_row = [1] * (len(row) + 1)

        for i in range(len(row) - 1):
            next_row[i + 1] = row[i] + row[i + 1]
        return next_row

    curr_row = [1]

    # O(row_idx)
    for i in range(row_idx):
        curr_row = generate_next_row(curr_row)

    return curr_row



def test():
    assert get_row(0) == [1]
    assert get_row(1) == [1, 1]
    assert get_row(2) == [1, 2, 1]
    assert get_row(4) == [1, 4, 6, 4, 1]