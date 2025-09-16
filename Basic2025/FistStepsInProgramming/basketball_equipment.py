annual_fee = int(input())

price_for_shoes = annual_fee - (annual_fee * 0.4)
price_for_equipment = price_for_shoes - (price_for_shoes * 0.2)
price_for_ball = price_for_equipment / 4
price_for_accessories = price_for_ball / 5
total_amount_for_equipment = (annual_fee + price_for_shoes + price_for_equipment + price_for_ball
                              + price_for_accessories)

print(total_amount_for_equipment)