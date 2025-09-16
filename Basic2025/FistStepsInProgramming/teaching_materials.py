number_pack_of_pens = int(input())
number_pack_of_markers = int(input())
liters_of_board_cleaner = int(input())
discount = int(input())

# •	Пакет химикали - 5.80 лв.
# •	Пакет маркери - 7.20 лв.
# •	Препарат - 1.20 лв (за литър)

price_of_pens = number_pack_of_pens * 5.80
price_of_markers = number_pack_of_markers * 7.20
price_of_board_cleaner = liters_of_board_cleaner * 1.20

price_for_all_materials = price_of_pens + price_of_markers + price_of_board_cleaner

price_with_discount = price_for_all_materials - (price_for_all_materials * discount/100)

print(round(price_with_discount, 2))