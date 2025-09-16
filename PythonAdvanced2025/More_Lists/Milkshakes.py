from collections import deque

chocolates = list(map(int, input().split(", ")))
milk = deque(map(int, input().split(", ")))

milkshakes = 0

while chocolates and milk and milkshakes < 5:
    current_chocolates = chocolates[-1]
    current_milk = milk[0]

    if current_chocolates <= 0 and current_milk <= 0:
        chocolates.pop()
        milk.popleft()
        continue
    if current_chocolates <= 0:
        chocolates.pop()
        continue
    if current_milk <= 0:
        milk.popleft()
        continue

    if current_chocolates == current_milk:
        chocolates.pop()
        milk.popleft()
        milkshakes += 1
        if milkshakes == 5:
            break
    else:
        milk.append(milk.popleft())
        chocolates[-1] -= 5

if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

print(f"Chocolate: {', '.join(map(str, chocolates)) if chocolates else 'empty'}")
print(f"Milk: {', '.join(map(str, milk)) if milk else 'empty'}")