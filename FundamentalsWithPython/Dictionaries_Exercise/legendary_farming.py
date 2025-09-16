materials = {"shards": 0, "fragments": 0, "motes": 0}
junk = {}

while True:
    parts = input().split()
    for idx in range(0, len(parts), 2):
        quantity = int(parts[idx])
        material = parts[idx + 1].lower()

        if material not in materials:
            materials[material] += quantity
            if materials[material] >= 250:
                materials[material] -= 250
                obtained = material
                break
        else:
            if material not in junk:
                junk[material] = 0
            junk[material] += quantity




