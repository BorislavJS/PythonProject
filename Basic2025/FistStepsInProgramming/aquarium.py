lenght = int(input())
width = int(input())
height = int(input())
rate = float(input())

aquarium_volume = lenght * width * height
liter_volume = aquarium_volume / 1000
trapped_space = rate / 100
needed_liters = liter_volume * (1 - trapped_space)

print(needed_liters)
