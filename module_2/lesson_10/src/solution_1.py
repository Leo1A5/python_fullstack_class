def finish_price(price, amount):
    if amount >= 10 and amount < 20:
        return int(price*0.9) 
    elif amount >=20:
        return int(price*0.8)
    else:
        return int(price)
print(f"Итоговая сумма : {finish_price(100, 5)}") 
print(f"Итоговая сумма : {finish_price(200, 10)}")
print(f"Итоговая сумма : {finish_price(150, 20)}")    