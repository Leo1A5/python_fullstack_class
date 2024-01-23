def new_func(func):
    def outer(item, first_price, second_price):
        return f"Цена на {item} изменилась {first_price} > {second_price} "
    return outer


@new_func
def change_price(item, first_price, second_price):
    return new_price


print(change_price("Кресло", 5000, 4500))
print(change_price("Стол", 8000, 7600))