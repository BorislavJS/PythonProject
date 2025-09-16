clothes = list(map(int, input().split()))
rack_capacity = int(input())

racks_used = 1
current_load = 0

while clothes:
    piece = clothes.pop()
    if piece == 0:
        continue
    if current_load + piece <= rack_capacity:
        current_load += piece
        if current_load == rack_capacity:
            if clothes:
                racks_used += 1
                current_load = 0
    else:
        racks_used += 1
        current_load = piece

print(racks_used)