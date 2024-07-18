price_list = [99, 150, 200, 349, 501]


def round_price(price):
    new_price = list(dict.fromkeys(map(lambda x: round(x, -2), price)))
    return new_price


print(round_price(price_list))
