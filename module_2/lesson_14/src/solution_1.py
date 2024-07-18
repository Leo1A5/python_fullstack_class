def create_grey(shade_max):
    return [(i, i, i) for i in range (0, shade_max, 5)]


print(create_grey(250))