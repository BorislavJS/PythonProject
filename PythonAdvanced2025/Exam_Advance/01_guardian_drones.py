from collections import deque

mechanical_parts = list(map(int,input().split()))
power_cells = deque(map(int, input().split()))

drone_requirements = {
    "Sentinel-X": 100,
    "Viper-MKII": 85,
    "Aegis-7": 75,
    "Striker-R": 65,
    "Titan-Core": 55
}

assembled_drones = []
built_drones = set()

drones_by_power = sorted(drone_requirements.items(), key=lambda kvp: -kvp[-1])

while mechanical_parts and power_cells and len(built_drones) < 5:
    part = mechanical_parts.pop()
    cell = power_cells.popleft()
    power = part + cell

    matched = False

    for name, required in drone_requirements.items():
        if power == required and name not in built_drones:
            assembled_drones.append(name)
            built_drones.add(name)
            matched = True
            break

    if matched:
        continue

    for name, required in drones_by_power:
        if required < power and name not in built_drones:
            assembled_drones.append(name)
            built_drones.add(name)
            new_cell_energy = cell - 30
            if new_cell_energy > 0:
                power_cells.append(new_cell_energy)
            matched = True
            break

    if not matched:
        new_cell_energy = cell - 1
        if new_cell_energy > 0:
            power_cells.append(new_cell_energy)

if len(built_drones) == 5:
    print("Mission Accomplished! All Guardian Drones activated!")
else:
    print("Mission Failed! Some drones were not built.")

if assembled_drones:
    print(f"Assembled Drones: {', '.join(assembled_drones)}")

if mechanical_parts:
    print(f"Mechanical Parts: {', '.join(map(str, reversed(mechanical_parts)))}")

if power_cells:
    print(f"Power Cells: {', '.join(map(str, power_cells))}")