products = {}

while True:
    line = input()
    if line == "buy":
        break

    name, price, quantity = line.split()
    price = float(price)
    quantity = int(quantity)

    if name not in products:
        products[name] = [price, quantity]
    else:
        # винаги обновяваме цената
        products[name][0] = price
        # добавяме и 0 количество, за да се запази името в списъка
        products[name][1] += quantity

for name, (price, quantity) in products.items():
    total = price * quantity
    print(f"{name} -> {total:.2f}")



