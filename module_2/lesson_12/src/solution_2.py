order1 = {"id": 1, "items": ["book", "pen"]}
order2 = {"id": 2, "items": []}
def check_order(order):
    return bool(order.get("items"))
def package_order(order):
    return f"Упакован заказ {order['id']}"
def send_order(check, package, order):
    if check(order):
        return f"Отправка: {order['id']}" # в этом случае работает
    else:
        return f"Отправка: {package} пуст" # в этом нет

print(send_order(check_order, package_order, order1))
print(send_order(check_order, package_order, order2))