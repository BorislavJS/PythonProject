from collections import deque

available_food = int(input())
orders = deque(map(int, input().split()))

print(max(orders))

while orders:
    current_order = orders[0]
    if available_food >= current_order:
        available_food -= current_order
        orders.popleft()
    else:
        break

if not orders:
    print("Orders complete")
else:
    print("Orders left:", *orders)