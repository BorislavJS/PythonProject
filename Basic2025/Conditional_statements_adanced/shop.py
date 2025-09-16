commodity = input()
town = input()
quantity = float(input())
unit_price = 0.0

# commodity -> coffee	water	beer	sweets	peanuts
# unit price -
# town -> Sofia Plovdiv Varna
if town == "Sofia":
    if commodity == "coffee":
        unit_price = 0.50
    elif commodity == "water":
        unit_price = 0.80
    elif commodity == "beer":
        unit_price = 1.20
    elif commodity == "sweets":
        unit_price = 1.45
    elif commodity == "peanuts":
        unit_price = 1.60

elif town == "Plovdiv":
    if commodity == "coffee":
        unit_price = 0.40
    elif commodity == "water":
        unit_price = 0.70
    elif commodity == "beer":
        unit_price = 1.15
    elif commodity == "sweets":
        unit_price = 1.30
    elif commodity == "peanuts":
        unit_price = 1.50

elif town == "Varna":
    if commodity == "coffee":
        unit_price = 0.45
    elif commodity == "water":
        unit_price = 0.70
    elif commodity == "beer":
        unit_price = 1.10
    elif commodity == "sweets":
        unit_price = 1.35
    elif commodity == "peanuts":
        unit_price = 1.55

total_price = quantity * unit_price
print(total_price)