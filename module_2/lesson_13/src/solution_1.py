order1 = {"id": 1, "items": ["book", "pen"]}
order2 = {"id": 2, "items": []}

def check_order(order):
    return bool(order.get("items"))
def package_order(check, order):
    if check(order) == True:
        return f"Упакован заказ {order['id']}"
def send_order(check, package, order):
    return f"Отправка: {package}"

print(check_order(package_order(), order)