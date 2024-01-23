import time


def timer(param):
    def outer(*arg, **kwargs):
         start = time.perf_counter()
         param(*arg, **kwargs)
         stop = time.perf_counter()
         print(f"Exectution: {round(stop-start, 2)} seconds")
    return outer


@timer
def create_design(name, stop):
    time.sleep(stop)
    print(name)
     

name_1 = "Логотип Васильевский рынок"
name_2 = "Макет сайта Логомашины"
create_design(name_1, 2.45)
create_design(name_2, 4.3)