min_number = None

while True:
    user_input = input()

    if user_input == "Stop":
        break

    number = int(user_input)
    if min_number is None or number < min_number:
        min_number = number

print(min_number)