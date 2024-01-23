base = {"arg": None , 
        "new_arg": None}


def second_outer(param):
    def outer(*args):
        if base["arg"] == args:
            return f"Загрузили из кеша: {base['new_arg']}"
        else:
            new_arg = param(*args)
            base["arg"] = args
            base["new_arg"] = new_arg
            return f"Посчитали цену: {new_arg}"
    return outer

        
@second_outer
def calculate_project_cost(*args):
    return 3000


print(calculate_project_cost('Логотип','Малый бизнес'))
print(calculate_project_cost('Логотип','Малый бизнес'))
