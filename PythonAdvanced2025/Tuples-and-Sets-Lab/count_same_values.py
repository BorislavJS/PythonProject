numbers = input().split()

formatted_numbers = [f"{float(num):.1f}" for num in numbers]

counts = {}

for number in formatted_numbers:
    if number in counts:
        counts[number] += 1
    else:
        counts[number] = 1

for number, count in counts.items():
    print(f"{number} - {count} times")