price:float = float(input("Цена товара: "))
USD:float = float(input("Курс доллара: "))
print("Сумма в рублях: ", round(price*USD, 1))