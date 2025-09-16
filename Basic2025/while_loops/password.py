# username = input("Type user name: ")
# user_password = input("Type your pass: ")
#
# data = input("Type pass: ")
# while data != user_password:
#     data = input("Wrong pass try again: ")
#
# print(f"Welcome {username}!")

user_name = input("Insert user name: ")
user_password = input("Insert password: ").strip()

data = input("type your pass: ").strip()
while data != user_password:
    data = input("Wrong pass try again: ").strip()

print(f"Welcome {user_name}")


# username = input("Type user name: ")
# user_password = input("Type your pass: ").strip()
#
# data = input("Type pass: ").strip()
# while data != user_password:
#     print(f"DEBUG: Expected {user_password}, but got {data}")  # За дебъгване
#     data = input("Wrong pass try again: ").strip()
#
# print(f"Welcome {username}!")