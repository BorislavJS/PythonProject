student_name = input()
current_class = 1
fail_count = 0
sum_grades = 0

while current_class <= 12:
    grade = float(input())

    if grade < 4.00:
        fail_count += 1
        if fail_count > 1:
            print(f"{student_name} has been excluded at {current_class} grade")
            break
    else:
        sum_grades += grade
        current_class += 1
else:
    average_grade = sum_grades / 12
    print(f"{student_name} graduated. Average grade: {average_grade:.2f}")

