elements = input().split()

bakery = {}

for idx in range(0, len(elements), 2):
    key = elements[idx]
    value = elements[idx + 1]
    bakery[key] = int(value)

searched_product = input().split()

for product in searched_product:
    if product in bakery:
        print(f'We have {bakery[product]} of {product} left')
    else:
        print(f"Sorry, we don't have {product}")