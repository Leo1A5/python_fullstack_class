def choose_ad_platform(money):
    if money < 1000:
        company = "Google"
        return company
    elif money >= 1000 and money < 5000:
        company = "Facebook"
        return company
    elif money >= 5000:
        company = "Instagram"
        return company
print(choose_ad_platform(500))
print(choose_ad_platform(3000))
print(choose_ad_platform(6000))    