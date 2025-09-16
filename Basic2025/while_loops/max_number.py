max_number = None

while True:
    user_input = input()

    if user_input == "Stop":
        break

    number = int(user_input)
    if max_number is None or number > max_number:
        max_number = number

print(max_number)