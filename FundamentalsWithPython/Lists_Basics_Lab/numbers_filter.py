# n = int(input())
#
# even_list = []
# odd_list = []
# negative_list = []
# positive_list = []
#
# for _ in range(n):
#     number = int(input())
#
#     if number >= 0:
#         positive_list.append(number)
#     else:
#         negative_list.append(number)
#
#     if number % 2 == 0:
#         even_list.append(number)
#     else:
#         odd_list.append(number)
#
# command = input()
#
# if command == "even":
#     print(even_list)
# elif command == "odd":
#     print(odd_list)
# elif command == "positive":
#     print(positive_list)
# else:
#     print(negative_list)

n = int(input())

numbers = []
filtered = []

for _ in range(n):
    current_number = int(input())
    numbers.append(current_number)

command = input()

if command == "even":
    for number in numbers:
        if number % 2 == 0:
            filtered.append(number)
elif command == "odd":
    for number in numbers:
        if number % 2 != 0:
            filtered.append(number)
elif command == "negative":
    for number in numbers:
        if number < 0:
            filtered.append(number)
elif command == "positive":
    for number in numbers:
        if number >= 0:
            filtered.append(number)

print(filtered)