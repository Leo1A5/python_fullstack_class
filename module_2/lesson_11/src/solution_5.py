days_1 = 30
days_2 = 31
def sales_schedule_with_while(day):
    print("Дни распродаж:", list(range(3, day + 1, 3)), sep = "")

sales_schedule_with_while(days_1)
sales_schedule_with_while(days_2)
