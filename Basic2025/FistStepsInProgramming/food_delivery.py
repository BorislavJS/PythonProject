import math

number_chicken_menu = int(input())
number_fish_menu = int(input())
number_vegan_menu = int(input())

price_for_chicken_menu = number_chicken_menu * 10.35
price_for_fish_menu = number_fish_menu * 12.40
price_for_vegan_menu = number_vegan_menu * 8.15
total_amount_for_menu = price_for_chicken_menu + price_for_fish_menu + price_for_vegan_menu
price_for_dessert = total_amount_for_menu * 0.2
price_for_delivery = 2.50
total_amount_for_delivery = total_amount_for_menu + price_for_dessert + price_for_delivery


print(f"{total_amount_for_delivery:.2f}")
