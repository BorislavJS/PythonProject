from collections import deque

packages = list(map(int,input().split()))
couriers = deque(map(int, input().split()))

total_weight = 0

while packages and couriers:
    package = packages[-1]
    courier = couriers[0]

    if courier >= package:
        total_weight += package
        packages.pop()
        couriers.popleft()

        if courier > package:
            new_capacity = courier - 2 * package
            if new_capacity > 0:
                couriers.append(new_capacity)
            else:
                pass
    else:
        delivered = courier
        remaining = package - courier
        total_weight += delivered
        packages.pop()
        if remaining > 0:
            packages.append(remaining)
        couriers.popleft()

print(f"Total weight: {total_weight} kg")

if not packages and not couriers:
    print("Congratulations, all packages were delivered successfully by the couriers today.")
elif packages and not couriers:
    print(f"Unfortunately, there are no more available couriers to deliver the following packages: {', '.join(map(str, packages))}")
elif not packages and couriers:
    print(f"Couriers are still on duty: {', '.join(map(str, couriers))} but there are no more packages to deliver.")



