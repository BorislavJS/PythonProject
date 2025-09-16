# numbers = list(input())
# stack = []
#
# for num in range(len(numbers)):
#     stack.append(numbers.pop())
#
# print("".join(stack))

# numbers = list(input())
# stack = []
#
# for _ in range(len(numbers)):
#     stack.append(numbers.pop())
#
# print("".join(stack))


# numbers = input().split()  # Разделя входа по интервали => ['1', '2', '3']
# stack = []
#
# for num in numbers:
#     stack.append(num)
#
# # Извеждаме числата в обратен ред
# while stack:
#     print(stack.pop(), end=' ')


# numbers = input().split()
# stack = []
#
# for num in numbers:
#     stack.append(num)
#
# while stack:
#     print(stack.pop(), end=" ")


# numbers = input().split()
# stack = []
#
# for num in numbers:
#     stack.append(num)
#
# while stack:
#     print(stack.pop(), end=" ")

# stack = []
#
# for num in map(int, input().split()):
#     stack.append(num)
#
# while stack:
#     print(stack.pop(), end=" ")

# stack = list(map(int, input().split()))
#
# while stack:
#     print(stack.pop(), end=" ")

stack = list(map(int, input().split()))
stack.reverse()
print(*stack)