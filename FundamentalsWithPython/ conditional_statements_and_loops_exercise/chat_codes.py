# n = int(input())
#
# for _ in range(n):
#     number = int(input())
#
#     if number == 88:
#         print("Hello")
#     elif number == 86:
#         print("How are you?")
#     elif number < 88:
#         print("GREAT!")
#     elif number > 88:
#         print("Bye.")

n = int(input())

responses = {
    88: "Hello",
    86: "How are you?"
}

for _ in range(n):
    number = int(input())

    if number in responses:
        print(responses[number])
    elif number < 88:
        print("GREAT!")
    else:
        print("Bye.")
