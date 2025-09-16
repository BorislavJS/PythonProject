from math import pi

figures = (input("Please insert figures: ")).lower()

if figures == "square":
    lengh = float(input())
    print(f"{lengh * lengh:.3f}")
elif figures == "rectangle":
    rectangle_a = float(input())
    rectangle_b = float(input())
    print(f"{rectangle_a * rectangle_b:.3f}")
elif figures == "circle":
    circle_radius = float(input())
    print(f"{pi * (circle_radius ** 2):.3f}")
elif figures == "triangle":
    triangle_lengh = float(input())
    triangle_heigh = float(input())
    print(f"{(triangle_lengh * triangle_heigh) / 2:.3f}")
else:
    print("Wrong figure!")


# from math import pi
#
# figure = input("Въведете фигура (square, rectangle, circle, triangle): ").lower()
#
# if figure == "square":
#     length = float(input("Въведете дължина на страната: "))
#     print(f"Лице на квадрата: {length * length:.3f}")
# elif figure == "rectangle":
#     rectangle_a = float(input("Въведете дължина: "))
#     rectangle_b = float(input("Въведете ширина: "))
#     print(f"Лице на правоъгълника: {rectangle_a * rectangle_b:.3f}")
# elif figure == "circle":
#     circle_radius = float(input("Въведете радиус: "))
#     print(f"Лице на кръга: {pi * (circle_radius ** 2):.3f}")
# elif figure == "triangle":
#     triangle_length = float(input("Въведете дължина на основата: "))
#     triangle_height = float(input("Въведете височина: "))
#     print(f"Лице на триъгълника: {(triangle_length * triangle_height) / 2:.3f}")
# else:
#     print("Невалидна фигура! Опитайте отново.")

