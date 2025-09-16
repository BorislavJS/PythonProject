bakery = {}

while True:
    command = input()
    if command == "statistics":
        break
    tokens = command.split(": ")
    product = tokens[0]
    quantity = int(tokens[1])
    if product not in bakery:
        bakery[product] = 0
    bakery[product] += quantity

print("Products in stock:")
for key, value in bakery.items():
    print(f"- {key}: {value}")
print(f"Total Products: {len(bakery)}")
print(f"Total Quantity: {sum(bakery.values())}")