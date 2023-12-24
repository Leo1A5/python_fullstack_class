def calculate_discount(prices):
    price_list = prices[:-1]
    discount = sum(price_list) * (prices[-1] / 100)
    return discount

print(f"Сумма скидки: {calculate_discount([100, 200, 300, 10])}")
print(f"Сумма скидки: {calculate_discount([50, 150, 250, 20])}")
