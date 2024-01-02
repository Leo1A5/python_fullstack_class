prices = (100, 200, 300, 400)
def calculate_discount():
    prices_first = prices[0] * 0.9
    mapped_numbers = list(map(lambda prices: prices - prices_first, prices))
    
    return mapped_numbers
finish_price = calculate_discount(prices)
print(finish_price)