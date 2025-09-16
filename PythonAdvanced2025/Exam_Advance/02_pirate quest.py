n = int(input())

matrix = []
ship = []
durability = 100
treasures = 0
charm_used = False

for row in range(n):
    row_data = list(input())
    matrix.append(row_data)
    for col in range(len(row_data)):
        if row_data[col] == "S":
            ship = [row, col]
        elif row_data[col] == "*":
            treasures += 1

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

matrix[ship[0]][ship[1]] = "."

while True:
    command = input()

    if command == "stop":
        break

    move = directions[command]
    r = (ship[0] + move[0]) % n
    c = (ship[1] + move[1]) % n

    cell = matrix[r][c]

    if cell == "*":
        treasures -= 1
        matrix[r][c] = "."

    elif cell == "C":
        if not charm_used:
            durability += 25
            if durability > 100:
                durability = 100
            charm_used = True
        matrix[r][c] = "."

    elif cell == "M":
        durability -= 25
        matrix[r][c] = "."
        if durability <= 0:
            ship = [r, c]
            print(f"Shipwreck! Last known coordinates ({ship[0]}, {ship[1]})")
            print(f"Ship Durability: 0")
            if treasures > 0:
                print(f"Unclaimed chests: {treasures}")
            matrix[ship[0]][ship[1]] = "S"
            [print(*row, sep='') for row in matrix]
            exit()

    ship = [r, c]

    if treasures == 0:
        print("Yo-ho-ho! All treasure chests collected!")
        print(f"Ship Durability: {durability}")
        matrix[ship[0]][ship[1]] = "S"
        [print(*row, sep='') for row in matrix]
        exit()

if treasures > 0:
    print("Retreat! Some treasures remain unclaimed.")
else:
    print("Yo-ho-ho! All treasure chests collected!")

print(f"Ship Durability: {durability}")

if treasures > 0:
    print(f"Unclaimed chests: {treasures}")

matrix[ship[0]][ship[1]] = "S"
[print(*row, sep='') for row in matrix]





