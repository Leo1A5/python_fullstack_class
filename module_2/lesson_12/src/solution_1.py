data_1 = [1, 2, 3, 4, 5]
data_2 = [10, 15, 5, 20]
def collect_data(data):
    process_data(data)
    return data
def process_data(data):
    mid_data = sum(data)/len(data)
    return mid_data
def summarize_data(mid_data):
    print(f"Итог: Среднее значение: {mid_data}")
collect_data(data_1)
collect_data(data_2)