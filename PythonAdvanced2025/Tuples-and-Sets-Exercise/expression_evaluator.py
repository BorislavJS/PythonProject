from collections import deque
print("Enter expression (e.g. 2 3 4 +):")
expression = input().split()

numbers = deque()

for token in expression:
    if token in "+-*/":
        result = numbers.popleft()
        while numbers:
            if token == "+":
                result += numbers.popleft()
            elif token == "-":
                result -= numbers.popleft()
            elif token == "*":
                result *= numbers.popleft()
            elif token == "/":
                result //= numbers.popleft()

        numbers.append(result)

    else:
        numbers.append(int(token))

print(numbers[0])
