def back_color(hours):
    if hours >= 18 or hours <= 6:
        color ="Темный"
        return color 
    else:
        color = "Светлый"
        return color
print(f"Цвет фона : {back_color(10)}") 
print(f"Цвет фона : {back_color(20)}")
print(f"Цвет фона : {back_color(5)}")         