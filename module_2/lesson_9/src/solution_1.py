price_list = [float(x) for x in input("Введите цены и скидку: ").split()]
def calculate_discount(prices):
    price_list = prices[:-1]
    discount = sum(price_list) * (prices[-1] / 100)
    return discount

total_discount = calculate_discount(price_list)

print("Сумма скидки: ", total_discount)

