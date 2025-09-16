from collections import deque

main_colors = {"red", "yellow", "blue"}
secondary_colors = {"orange": {"red", "yellow"}, "purple": {"red", "blue"},
                    "green": {"yellow", "blue"}}

input_data = input().split()
data = deque(input_data)

found_color = []

while data:
    if len(data) >= 2:
        first = data.popleft()
        last = data.pop()
    else:
        first = data.pop()
        last = ""

    combo_one = first + last
    combo_two = last + first

    if combo_one in main_colors or combo_one in secondary_colors:
        found_color.append(combo_one)
    elif combo_two in main_colors or combo_two in secondary_colors:
        found_color.append(combo_two)
    else:
        first = first[:-1]
        last = last[:-1]
        mid_index = len(data) // 2
        if last:
            data.insert(mid_index, last)
        if first:
            data.insert(mid_index, first)

valid_color = []

for color in found_color:
    if color in main_colors:
        valid_color.append(color)
    elif color in secondary_colors:
        required = secondary_colors[color]
        if required.issubset(set(found_color)):
            valid_color.append(color)

print(valid_color)