# n = int(input())
#
# for num in range(1, n+1):
#     is_special = False
#     num_as_string = str(num)
#     sum_digit = 0
#     for ch in num_as_string:
#         sum_digit += int(ch)
#
#     if sum_digit == 5 or sum_digit == 7 or sum_digit == 11:
#         is_special = True
#     print(f"{num} -> {is_special}")



n = int(input())

for num in range(1, n + 1):
    sum_digits = 0
    digits = num

    while digits > 0:
        sum_digits += digits % 10
        digits = int(digits / 10)

    if sum_digits == 5 or sum_digits == 7 or sum_digits == 11:
        print(f"{num} -> True")
    else:
        print(f"{num} -> False")





