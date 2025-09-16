first_set = set(map(int, input().split()))
second_set = set(map(int, input().split()))

n = int(input())

for _ in range(n):
    command_parts = input().split()
    action = command_parts[0]
    target = command_parts[1]
    numbers = map(int, command_parts[2:])

    if action == "Add":
        if target == "First":
            first_set.update(numbers)
        elif target == "Second":
            second_set.update(numbers)

    elif action == "Remove":
        if target == "First":
            for num in numbers:
                first_set.discard(num)
        elif target == "Second":
            for num in numbers:
                second_set.discard(num)

    elif action == "Check" and target == "Subset":
        if first_set.issubset(second_set) or second_set.issubset(first_set):
            print("True")
        else:
            print("False")

print(", ".join(map(str, sorted(first_set))))
print(", ".join(map(str, sorted(second_set))))
