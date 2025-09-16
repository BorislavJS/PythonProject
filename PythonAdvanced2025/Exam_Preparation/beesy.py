# n = int(input())
# field = [list(input()) for _ in range(n)]
#
# bee_row, bee_col = 0, 0
# for r in range(n):
#     for c in range(n):
#         if field[r][c] == 'B':
#             bee_row, bee_col = r, c
#             break
#
# energy = 15
# nectar = 0
# restored_energy = False
#
# directions = {
#     'up': (-1, 0),
#     'down': (1, 0),
#     'left': (0, -1),
#     'right': (0, 1)
# }
#
# field[bee_row][bee_col] = '-'
#
# while True:
#     try:
#         command = input()
#     except EOFError:
#         break
#
#     dr, dc = directions[command]
#     bee_row = (bee_row + dr) % n
#     bee_col = (bee_col + dc) % n
#     energy -= 1
#
#     cell = field[bee_row][bee_col]
#
#     if cell.isdigit():
#         nectar += int(cell)
#         field[bee_row][bee_col] = '-'
#
#     elif cell == 'H':
#         if nectar >= 30:
#             print(f"Great job, Beesy! The hive is full. Energy left: {energy}")
#         else:
#             print("Beesy did not manage to collect enough nectar.")
#         field[bee_row][bee_col] = 'B'
#         break
#
#     # Проверка дали енергията е на 0
#     if energy == 0:
#         if nectar >= 30 and not restored_energy:
#             # Възстановяване на енергия
#             restored_energy = True
#             diff = nectar - 30
#             energy += diff
#             nectar = 30
#             if energy == 0:
#                 print("This is the end! Beesy ran out of energy.")
#                 field[bee_row][bee_col] = 'B'
#                 break
#         else:
#             print("This is the end! Beesy ran out of energy.")
#             field[bee_row][bee_col] = 'B'
#             break
#
# if field[bee_row][bee_col] != 'B':
#     field[bee_row][bee_col] = 'B'
#
# for row in field:
#     print(''.join(row))

n = int(input())
field = [list(input()) for _ in range(n)]

bee_row, bee_col = 0, 0
for r in range(n):
    for c in range(n):
        if field[r][c] == 'B':
            bee_row, bee_col = r, c
            break

energy = 15
nectar = 0
restored_energy = False

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

field[bee_row][bee_col] = '-'

while True:
    try:
        command = input()

        if command not in directions:
            continue  # Игнорирай невалидни команди

        dr, dc = directions[command]
        bee_row = (bee_row + dr) % n
        bee_col = (bee_col + dc) % n
        energy -= 1

        cell = field[bee_row][bee_col]

        if cell.isdigit():
            nectar += int(cell)
            field[bee_row][bee_col] = '-'

        elif cell == 'H':
            if nectar >= 30:
                print(f"Great job, Beesy! The hive is full. Energy left: {energy}")
            else:
                print("Beesy did not manage to collect enough nectar.")
            field[bee_row][bee_col] = 'B'
            break

        if energy == 0:
            if nectar >= 30 and not restored_energy:
                restored_energy = True
                diff = nectar - 30
                energy += diff
                nectar = 30
                if energy == 0:
                    print("This is the end! Beesy ran out of energy.")
                    field[bee_row][bee_col] = 'B'
                    break
            else:
                print("This is the end! Beesy ran out of energy.")
                field[bee_row][bee_col] = 'B'
                break

    except EOFError:
        break
