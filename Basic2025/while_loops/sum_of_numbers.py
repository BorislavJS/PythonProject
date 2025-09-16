constant_number = int(input())
sum_numbers_counter = 0

while True:
    current_numbers = int(input())
    sum_numbers_counter += current_numbers

    if sum_numbers_counter >= constant_number:
        print(sum_numbers_counter)
        break



