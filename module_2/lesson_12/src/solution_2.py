order1 = {"id": 1, "items": ["book", "pen"]}
order2 = {"id": 2, "items": []}
def check_order(order):
    global check
    check = bool(order.get("items"))
    return check
def package_order(check, order):
    if check:
        package = f"Упакован заказ: {order['id']}"
        return package
    else:
        return f"Заказ {order['id']}: пуст"
def send_order(check, package, order):
    return f"Отправка: {package}"


print(send_order(check_order(order1), package_order(check, order1), order1))
print(send_order(check_order(order2), package_order(check, order2), order2))