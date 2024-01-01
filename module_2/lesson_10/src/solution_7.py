prices = (100, 200, 300, 400)
def calculate_discount(prices, index=0, previous_price=None):
    end_prices = []

    if index < len(prices):
        current_price = prices[index] 
        current_discount = previous_price * 0.1 if previous_price is not None else 0
        discount_price = current_price - current_discount if previous_price is not None else current_price
        end_prices.append(discount_price)
        end_prices += calculate_discount(prices, index + 1, current_price)

    return end_prices
print(calculate_discount(prices))
"""1000, 2000, 3000
5000, 10000, 15000
100, 200, 300, 400
50, 100"""
