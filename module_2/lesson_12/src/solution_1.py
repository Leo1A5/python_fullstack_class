data_1 = [1, 2, 3, 4, 5]
data_2 = [10, 15, 5, 20]
def collect_data(data):
    return data
def process_data(data):
    mid_data = sum(data)/len(data)
    return mid_data
def summarize_data(mid_data):
    print(f"Итог: Среднее значение: {mid_data}")
base_data_1 = collect_data(data_1)
mid_base_1 = process_data(base_data_1)
summarize_1 = summarize_data(mid_base_1)

base_data_2 = collect_data(data_2)
mid_base_2 = process_data(base_data_2)
summarize_2 = summarize_data(mid_base_2)