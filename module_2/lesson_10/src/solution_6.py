price_list = [10, 8, 12]
def find_max_price(price_list):
    if len(price_list) == 0:
        return None
    elif len(price_list) == 1:
        return price_list[0]
    else:
        max_price = find_max_price(price_list[1:])
        return price_list[0] if price_list[0] > max_price else max_price

result = find_max_price(price_list)
print(result)
"""15, 7, 9
1, 10, 20, 5
25, 25, 25
10, 8, 12"""