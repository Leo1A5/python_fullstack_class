rgb = [int(x) for x in input("RGB: ").split()]
def convert_to_hex(rgb):
    if len(rgb) != 3:
        print("Ошибка")
    hex_color = f"#{rgb[0]:02X}{rgb[1]:02X}{rgb[2]:02X}"
    return hex_color

hex_format = convert_to_hex(rgb)
print(hex_format)