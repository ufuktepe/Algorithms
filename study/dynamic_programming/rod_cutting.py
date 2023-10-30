

def get_max_price(rod_length, price, max_prices):
    if max_prices[rod_length] is not None:
        return max_prices[rod_length]

    max_price = float('-inf')
    for i in range(1, rod_length + 1):
        curr_price = price[i] + get_max_price(rod_length - i, price, max_prices)
        if max_price < curr_price:
            max_price = curr_price

    max_prices[rod_length] = max_price
    return max_price


def rod_cutting_top_down(rod_length, price):
    max_prices = [None for _ in range(rod_length + 1)]
    max_prices[0] = 0
    max_prices[1] = price[1]

    get_max_price(rod_length, price, max_prices)

    return max_prices


def rod_cutting_bottom_up(rod_length, price):
    max_prices = [None for _ in range(rod_length + 1)]
    s = [None for _ in range(rod_length + 1)]  # The optimal size of the first piece to cut off.
    max_prices[0] = 0
    s[0]

    for length in range(1, rod_length + 1):
        max_prices[length] = price[length]
        s[length] = length
        for suffix_length in range(1, length + 1):
            curr_price = max_prices[length - suffix_length] + price[suffix_length]
            if max_prices[length] < curr_price:
                max_prices[length] = curr_price
                s[length] = suffix_length

    return max_prices, s


if __name__ == '__main__':
    price = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
    max_prices, s = rod_cutting_bottom_up(10, price)
    # max_prices = rod_cutting_top_down(10, price)

    for length, p in enumerate(max_prices):
        print(f'r{length} = {p}, first piece size={s[length]}')
