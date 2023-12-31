def analyze_ad_efficiency(click, show, views):
    point = click / show
    if point <= 0.01 and views > show:
        rating = "Недооцененная"
        return rating
    elif point > 0.01 and point < 0.05:
        rating = "Низкая"
        return rating
    elif point >= 0.05 and point <= 0.1 and views > click:
        rating = "Средняя"
        return rating
    elif point > 0.1:
        rating = "Высокая"
        return rating
    else:
        rating = "Неопределенная"
        return rating

print(analyze_ad_efficiency(50, 10000, 15000)) 
print(analyze_ad_efficiency(200, 10000, 5000))
print(analyze_ad_efficiency(700, 10000, 800))
print(analyze_ad_efficiency(1200, 10000, 1000))
print(analyze_ad_efficiency(500, 10000, 200))       