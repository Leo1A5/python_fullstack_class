price_1 = [100, 200, 300]
price_2 = [15, 23, 39, 50]

def sum_sales_with_for(price):
    total = 0
    for num in price: 
        total += num  
    print(*price, sep = ' + ', end = f' = {total}\n')

sum_sales_with_for(price_1)
sum_sales_with_for(price_2)


