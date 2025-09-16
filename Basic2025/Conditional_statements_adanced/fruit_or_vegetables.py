name_of_product = input()

# fruit -> banana, apple, kiwi, cherry, lemon и grapes;
# vegetables -> tomato, cucumber, pepper и

if name_of_product == "banana" or name_of_product == "apple" or name_of_product == "kiwi"\
        or name_of_product == "cherry" or name_of_product == "lemon" or name_of_product == "grapes":
    print("fruit")
elif name_of_product == "tomato" or name_of_product == "cucumber" or name_of_product == "pepper"\
        or name_of_product == "carrot":
    print("vegetables")
else:
    print("Unknown")