n = int(input())
stack = []

for _ in range(n):
    reading_request = input().split()
    command = reading_request[0]

    if command == "1":
        number = int(reading_request[1])
        stack.append(number)
    elif command == "2":
        if stack:
            stack.pop()
    elif command == "3":
        if stack:
            print(max(stack))
    elif command == "4":
        if stack:
            print(min(stack))

print(", ".join(map(str, reversed(stack))))