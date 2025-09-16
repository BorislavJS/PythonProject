elements = input().split()

bakery = {}

for idx in range(0, len(elements), 2):
    key = elements[idx]
    value = elements[idx + 1]
    bakery[key] = int(value)

print(bakery)