product_list = {"apples": 50, "bananas" : 10, "cherries": 3}
def track_low_stock_with_for(product_list, value):
    print("Низкий запас:")
    for k, v in product_list.items():
        if v <= 15:
           print(f"{k} - {v}")
track_low_stock_with_for(product_list, value = 15)