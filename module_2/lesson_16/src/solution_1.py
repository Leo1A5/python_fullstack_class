input_length = input("Введите длины полок: ")
length_shelves = [int(x) for x in input_length.split(",")]


def create_shelves(length_shelves):
    shelves = [[length, 0] for length in length_shelves]
    return shelves


finished_shelves = create_shelves(length_shelves)

print(f"Полки: {finished_shelves}")