# numbers_list = [10, 20, 30, 40, 50]
#
#
# for num in numbers_list:
#     if num % 2 != 0:
#         print(num)


# numbers_list = [10, 20, 30, 40, 50]
#
# square_list = []
#
# for num in numbers_list:
#     square_list.append(num ** 2)
#
# print(square_list)


# names_list = ["ivan", "maria", "petar"]
#
# for i, value in enumerate(names_list):
#     print(i, value)


# nums = [1, 2, 3]
# squares = []
# for n in nums:
#     squares.append(n * n)
# print(squares)



# name = input("Въведи име: ")

# insert_name = input()
# names_list = ["Ivan", "Borko", "Pesho"]
#
# for name in names_list:
#     if insert_name in names_list:
#         print(insert_name)
#         break


# insert_name = input()
#
# names_list = ["Pesho", "Gosho", "Maria"]
#
# if insert_name in names_list:
#     print(f"Името го има: {insert_name}")
# else:
#     print(f"Не е в списъка: {insert_name}")


# numbers_list = [1, 1, 2, 33, 6, 7, 33, 5, 5]
#
# if len(numbers_list) > 5:
#     print(f"Long list")
# else:
#     print(f"Short list")


# insert_number = int(input("Insert number: "))
#
# numbers_list = [1, 1, 2, 33, 6, 7, 33, 5, 5]
#
# if insert_number in numbers_list:
#     print(f"The number is in the list {insert_number}")
# else:
#     print(f"The number is not in the list")

# list_of = ["a", "b", "c", "d"]
#
# print(len(list_of))


# list_one = [1, 5, 7,  19]
# list_two = [2, 6, 78, 14]
#
# new_list = list_one + list_two
#
# print(new_list)


# list_one = [1, 5, 7,  19]
# list_two = [2, 6, 78, 14]
#
# list_one.extend(list_two)
#
# print(list_one)



# list_one = [1, 4, 8, 10]
# list_two = [2, 5, 8, 11]
#
# for one, two in zip(list_one, list_two):
#     print(one + two)


# names_one = ["pesho", "Gosho", "Mariq", "Stefka"]
# names_two = ["Izabel", "Borko", "Mariq", "Ginka"]
#
# combined = list(set(names_one + names_two))
#
# print(combined)
#
#
#
# names_one = ["pesho", "Gosho", "Mariq", "Stefka"]
# names_two = ["Izabel", "Borko", "Mariq", "Ginka"]
#
# unique_name = []
#
# for name in names_one + names_two:
#     if name not in unique_name:
#         unique_name.append(name)
#
# print(unique_name)




# numbers_list = [1, 2, 4, 4, 5, 66, 77, 77, 8, 7, 888]
#
# unique_list = list(set(numbers_list))
#
# print(unique_list)





# numbers_list = [1, 2, 4, 4, 5, 66, 77, 77, 8, 7, 888]
#
# unique_list = []
#
# for number in numbers_list:
#     if number not in unique_list:
#         unique_list.append(number)
#
# print(unique_list)



# list1 = [1, 2, 3, 4, 4, 5]
# list2 = [3, 4, 4, 5, 6]
#
# common = list(set(list1) & set(list2))
# print(common)







# list_one = [1, 2, 3, 4, 4, 5]
# list_two = [3, 4, 4, 5, 6]
#
# common = []
#
# for num in list_one:
#     if num in list_two and num not in common:
#         common.append(num)
#
# print(common)



# # Потребителят въвежда числа, разделени със запетая
# user_input = input("Въведи числа, разделени със запетая: ")
#
# # Преобразуваме входа в списък от цели числа
# numbers_list = [int(x) for x in user_input.split(",")]
#
# # Създаваме списък с уникални стойности в реда на въвеждане
# unique_list = []
#
# for number in numbers_list:
#     if number not in unique_list:
#         unique_list.append(number)
#
# # Отпечатваме резултата
# print("Списък без повтарящи се елементи:", unique_list)


# # Въвеждане на имена, разделени със запетая
# user_input = input("Въведи имена, разделени със запетая: ")
#
# # Преобразуваме входа в списък от имена (с почистване на празни пространства)
# names_list = [name.strip() for name in user_input.split(",")]
#
# # Създаваме списък с уникални имена в реда на срещане
# unique_names = []
#
# for name in names_list:
#     if name not in unique_names:
#         unique_names.append(name)
#
# # Отпечатваме резултата
# print("Списък без повтарящи се имена:", unique_names)


# print("Въвеждай имена едно по едно. Напиши 'край' за край на въвеждането.")
#
# unique_names = []
#
# while True:
#     name = input("Име: ").strip()
#
#     if name.lower() == "край":
#         break
#
#     if name not in unique_names:
#         unique_names.append(name)
#
# print("Списък без повтарящи се имена:", unique_names)



# numbers_list = [1, 6, 5, 100, 7, 8, 99, 88]
#
# numbers_list.sort()
# print(numbers_list)




# numbers_list = [1, 6, 5, 100, 7, 8, 99, 88]
#
# numbers_list.sort(reverse=True)
# print(numbers_list)



# numbers_list = [1, 6, 5, 100, 7, 8, 99, 88]
#
# sorted_list = sorted(numbers_list)
#
# print(sorted_list)




# numbers_list = [1, 6, 5, 100, 7, 8, 99, 88]
#
# for i in range(len(numbers_list)):
#     for j in range(len(numbers_list) - 1):
#         if numbers_list[j] > numbers_list[j + 1]:
#             numbers_list[j], numbers_list[j + 1] = numbers_list[j + 1], numbers_list[j]
#
# print(numbers_list)

# numbers_list = [1, 6, 5, 100, 7, 8, 99, 88]
#
# sum_of_numbers = sum(numbers_list)
# print(sum_of_numbers)

# numbers_float = [abs(float(num)) for num in input().split()]

# word = list(input())
# word1 = input().split()
# print(word)
# print(word1)

text = list(input())
# stack = []

for i in range(len(text)):
    print(i)

# word = input()
#
# print(word[::-1])