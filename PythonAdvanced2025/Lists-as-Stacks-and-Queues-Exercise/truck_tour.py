n = int(input())

petrol_pumps = []

for _ in range(n):
    amount_of_petrol, distance_from_that_pump = map(int, input().split())
    petrol_pumps.append((amount_of_petrol, distance_from_that_pump))

start_index = 0
total_fuel = 0
current_fuel = 0

for idx in range(n):
    amount_of_petrol, distance_from_that_pump = petrol_pumps[idx]
    net = amount_of_petrol - distance_from_that_pump

    total_fuel += net
    current_fuel += net

    if current_fuel < 0:
        start_index = idx + 1
        current_fuel = 0

if total_fuel >= 0:
    print(start_index)



