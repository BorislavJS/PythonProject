square_meters_for_landscaped = float(input())

price_for_landscaped = square_meters_for_landscaped * 7.61
discount = price_for_landscaped * 0.18
final_price_for_landscaped = price_for_landscaped - discount

print(f"The final price is: {final_price_for_landscaped} lv.")
print(f"The discount is: {discount} lv.")