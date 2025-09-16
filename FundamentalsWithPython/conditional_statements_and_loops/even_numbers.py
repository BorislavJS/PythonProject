n = int(input())

for _ in range(n):
    number = int(input())
    if not number % 2 == 0:
        print(f"{number} is odd!")
        break
else:
    print("All numbers is even!")

# n = int(input())
#
# for _ in range(n):
#     number = int(input())
#     if number % 2 != 0:
#         print(f"{number} is odd!")
#         break
# else:
#     print("All numbers is even!")


# n = int(input())
#
# number_are_even = True
# for _ in range(n):
#     number = int(input())
#
#     if number % 2 != 0:
#         number_are_even = False
#         print(f"{number} is odd!")
#         break
#
# if number_are_even:
#     print("All numbers are even")



