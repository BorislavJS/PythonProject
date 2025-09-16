# group_size = int(input())
# days = int(input())
#
# coins = 0
# for day in range(1, days + 1):
#     if day % 10 == 0:
#         group_size -= 2
#
#     if day % 15 == 0:
#         group_size += 5
#         coins -= 2 * group_size
#
#     coins += 50 - 2 * group_size
#
#     if day % 3 == 0:
#         coins -= 3 * group_size
#
#     if day % 5 == 0:
#         coins += 20 * group_size
#
# coins_per_companion = coins // group_size
# print(f"{group_size } companions received {coins_per_companion} coins each.")

group_size = int(input())
days = int(input())

coins = 0
companions = group_size

for day in range(1, days + 1):
    # Every 10th day 2 companions leave
    if day % 10 == 0:
        companions -= 2
    # Every 15th day 5 companions join
    if day % 15 == 0:
        companions += 5

    # Earn daily coins
    coins += 50

    # Daily food expenses
    coins -= 2 * companions

    # Every 3rd day motivational party
    if day % 3 == 0:
        coins -= 3 * companions

    # Every 5th day boss fight
    if day % 5 == 0:
        coins += 20 * companions
        # Additional cost if party is also held
        if day % 3 == 0:
            coins -= 2 * companions

# Final calculation
coins_per_companion = coins // companions

print(f"{companions} companions received {coins_per_companion} coins each.")