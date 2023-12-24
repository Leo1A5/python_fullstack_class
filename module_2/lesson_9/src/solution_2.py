def convert_to_hex(rgb):
    if len(rgb) != 3:
        print("Ошибка")
    hex_color = f"#{rgb[0]:02X}{rgb[1]:02X}{rgb[2]:02X}"
    return hex_color


print(f"HEX: {convert_to_hex([255, 0, 0])}")
print(f"HEX: {convert_to_hex([0, 255, 0])}")
print(f"HEX: {convert_to_hex([0, 0, 255])}")