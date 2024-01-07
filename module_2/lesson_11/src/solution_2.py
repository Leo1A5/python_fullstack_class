items_list_1 = ["fruit", "toy", "fruit", "toy", "toy"]
items_list_2 = ["clothes", "clothes", "clothes", "clothes"]
search_1 = "toy"
search_2 = "clothes"
def count_specific_items_with_while(items, search):
    while search in items:
        count = items.count(search)
        print(f"Кол-во {search}: {count}")  
        break
count_specific_items_with_while(items_list_1, search_1)
count_specific_items_with_while(items_list_2, search_2)