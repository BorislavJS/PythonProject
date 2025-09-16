materials = {"shards": 0, "fragments": 0, "motes": 0}
junk = {}

while True:
    parts = input().split()
    obtained = None

    for idx in range(0, len(parts), 2):
        quantity = int(parts[idx])
        material = parts[idx + 1].lower()

        if material in materials:
            materials[material] += quantity
            if materials[material] >= 250:
                materials[material] -= 250
                obtained = material
                break
        else:
            if material not in junk:
                junk[material] = 0
            junk[material] += quantity

    if obtained:
        break

legendary_items = {
    "shards": "Shadowmourne",
    "fragments": "Valanyr",
    "motes": "Dragonwrath"
}

print(f"{legendary_items[obtained]} obtained!")

# Отпечатай ключовите материали по зададен ред
for material in ["shards", "fragments", "motes"]:
    print(f"{material}: {materials[material]}")

# Отпечатай junk-а в реда на появяване
for item, qty in junk.items():
    print(f"{item}: {qty}")




