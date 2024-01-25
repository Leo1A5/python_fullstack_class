base = {"arg": None , 
        "new_arg": None}


def check_cash(func):
    def wrap(*args):
        if base["arg"] == args:
            print(f"Загрузили из кеша: {base['new_arg']}")
        else:
            new_arg = func(*args)
            base["arg"] = args
            base["new_arg"] = new_arg
            print(f"Посчитали цену: {new_arg}")
        func(*args)
    return wrap

        
@check_cash
def calculate_project_cost(*args):
    return 3000


calculate_project_cost('Логотип','Малый бизнес')
calculate_project_cost('Логотип','Малый бизнес')
