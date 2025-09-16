from collections import deque

materials = list(map(int, input().split()))
magic = deque(map(int, input().split()))

needed_magic = {
    150: "Doll",
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle"
}

crafted = {}

while materials and magic:
    current_material = materials[-1]
    current_magic = magic[0]

    if current_material == 0 and current_magic == 0:
        materials.pop()
        magic.popleft()
        continue

    if current_material == 0:
        materials.pop()
        continue

    if current_magic == 0:
        magic.popleft()
        continue

    product = current_material * current_magic

    if product in needed_magic:
        toy = needed_magic[product]
        crafted[toy] = crafted.get(toy, 0) + 1
        materials.pop()
        magic.popleft()

    elif product < 0:
        materials.pop()
        magic.popleft()
        materials.append(current_material + current_magic)

    else:
        magic.popleft()
        materials[-1] += 15

success = (
    ("Doll" in crafted and "Wooden train" in crafted) or
    ("Teddy bear" in crafted and "Bicycle" in crafted)
)

if success:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join(map(str, reversed(materials)))}")

if magic:
    print(f"Magic left: {', '.join(map(str, magic))}")

for toy in sorted(crafted):
    print(f"{toy}: {crafted[toy]}")