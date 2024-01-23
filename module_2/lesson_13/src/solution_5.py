def second_outer(func):
    def outer(login, password):
        if login == "Роман" and password == "correctpassword":
            return func(login, password)
        else:
            return "В доступе отказано!"
    return outer


@second_outer
def access_client_data(login, password):
    return "Доступ получен. Данные:..."


print(access_client_data("Роман", "correctpassword"))
print(access_client_data("Олег", "wrongpassword"))