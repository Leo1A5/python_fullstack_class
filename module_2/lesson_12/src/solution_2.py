order1 = {"id": 1, "items": ["book", "pen"]}
order2 = {"id": 2, "items": []}
def check_order(order):
    return bool(order.get("items"))
def package_order(order):
    return bool(order)
def send_order(check, package, order):
    if check(order):
        return f"Отправка: Упакован заказ {order['id']}" if package(order) else f"Нечего упаковывать"
    else:
        return f"Отправка: заказ {order['id']} пуст"

print(send_order(check_order, package_order, order1))
print(send_order(check_order, package_order, order2))