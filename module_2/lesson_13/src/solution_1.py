def check_price(func):
    def wrap(*args):
        item, first_price, second_price = args 
        print(f"Цена на {item} изменилась {first_price} > {second_price} ")
        func(*args)
    return wrap


@check_price
def change_price(item, first_price, second_price):
    pass


change_price("Кресло", 5000, 4500)
change_price("Стол", 8000, 7600)