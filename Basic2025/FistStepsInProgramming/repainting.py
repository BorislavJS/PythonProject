needed_nylon = int(input())
needed_paint = int(input())
needed_thiner = int(input())
hour_for_work = int(input())

price_for_nylon = (needed_nylon + 2) * 1.50
price_for_paint = (needed_paint * 1.1) * 14.50
price_for_thiner = needed_thiner * 5.0
price_for_bag = 0.40

total_amount_for_materials = price_for_nylon + price_for_paint + price_for_thiner + price_for_bag
amount_for_craftsman = (total_amount_for_materials * 0.3) * hour_for_work
total_sum = total_amount_for_materials + amount_for_craftsman

print(total_sum)



