# def even_odd(*args: int, command: str):
#     if command.lower() == "even":
#         return [x for x in args if x % 2 == 0]
#     else:
#         return [x for x in args if x % 2 != 0]
from typing import Any

def even_odd(*args: Any):
    numbers = list(args)
    command = numbers.pop()
    if command.lower() == "even":
        return [num for num in numbers if num % 2 == 0 ]
    else:
        return [num for num in numbers if num % 2 != 0 ]


print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))



