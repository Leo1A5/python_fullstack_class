def second_outer(func):
    def outer(project_name,project_num, *args, **kwargs):
        if len(args) != 0 or len(kwargs) != 0:
            return "Ошибка: неверное колличество аргументов!"
        elif isinstance(project_name, str) == False:
            return "Ошибка: первый аргумент не строка!"
        elif isinstance(project_num, int) == False:
            return "Ошибка: второй аргумент не число!"
        return func(project_name, project_num)
    return outer


@second_outer
def estimate_time(project_name, project_num):
    return "Estimated time calculated successfully."


print(estimate_time("Веб-сайт", "пять"))
print(estimate_time("Визитка", 10))
