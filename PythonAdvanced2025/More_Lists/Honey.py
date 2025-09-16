from collections import deque

bees = deque(map(int, input().split()))
nectar = list(map(int, input().split()))
symbols = deque(input().split())

total_honey = 0

while bees and nectar:
    current_bee = bees[0]
    current_nectar = nectar[-1]

    if current_nectar < current_bee:
        nectar.pop()
        continue

    bees.popleft()
    nectar.pop()
    symbol = symbols.popleft()

    if symbol == "+":
        result = current_bee + current_nectar
        total_honey += abs(result)
    elif symbol == "-":
        result = current_bee - current_nectar
        total_honey += abs(result)
    elif symbol == "*":
        result = current_bee * current_nectar
        total_honey += abs(result)
    elif symbol == "/":
        if current_nectar == 0:
            continue
        result = current_bee / current_nectar
        total_honey += abs(result)

print(f"Total honey made: {total_honey}")

if bees:
    print(f"Bees left: {', '.join(map(str, bees))}")
if nectar:
    print(f"Nectar left: {', '.join(map(str, nectar))}")