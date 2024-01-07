unit = [[1, 2, 3], "meter"]
def convert_units_with_while(unit):
    unit_len = 0
    num = unit[0]
    system = unit[1]
    while unit_len < len(num):
        swap = float(num[unit_len]) * 3.28084
        print(f"{num[unit_len]} {system}(s) = {swap} foot(feet)")
        unit_len += 1
convert_units_with_while(unit)
