capacity = 255

n = int(input())
tank = 0
for _ in range(n):
    water_liters = int(input())
    if tank + water_liters > capacity:
        print("Insufficient capacity!")
    else:
        tank += water_liters
print(tank)

