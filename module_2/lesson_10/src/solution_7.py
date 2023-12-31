def calculate_discount(*early, **now,):
    finaly_price :float = now - (early * 0.1)
    return finaly_price
print(calculate_discount(1000, 2000, 3000))
print(calculate_discount(5000, 10000, 15000))
print(calculate_discount(100, 200, 300, 400))
print(calculate_discount(50, 100))