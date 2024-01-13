order1 = {"id": 1, "items": ["book", "pen"]}
order2 = {"id": 2, "items": []}

def check_order(order):
    return bool(order.get("items"))
def package_order(check, order):
    if check(order) == True:
        package = f"Упакован заказ: {order['id']}"
        return package
def send_order(check, package, order):
    if check == True:
        return f"Отправка: {package}"

print(send_order(check_order, package_order, order1))
print(send_order(check_order, package_order, order2))